import re
import argparse
import os

def clean_brackets_and_images(content):
    """
    Removes citation brackets and image references while preserving LaTeX expressions.
    """
    # Step 1: Identify and temporarily preserve LaTeX expressions
    latex_pattern = r'\[[^]]*?[\\\/\+\-\*\=\(\)\.\^\{\}][^]]*?\]'
    latex_expressions = re.findall(latex_pattern, content)
    
    # Temporarily replace LaTeX expressions with placeholders
    for i, expr in enumerate(latex_expressions):
        placeholder = f"LATEX_PLACEHOLDER_{i}"
        content = content.replace(expr, placeholder)
    
    # Step 2: Remove citation brackets containing alphanumeric chars, commas, spaces
    citation_pattern = r'\[[a-zA-Z0-9\s,]+\]'
    content = re.sub(citation_pattern, '', content)
    
    # Step 3: Remove image references
    image_pattern = r'!\[img-\d+\.jpeg\]\(img-\d+\.jpeg\)'
    content = re.sub(image_pattern, '', content)
    
    # Step 4: Restore LaTeX expressions
    for i, expr in enumerate(latex_expressions):
        placeholder = f"LATEX_PLACEHOLDER_{i}"
        content = content.replace(placeholder, expr)
    
    return content

def remove_sections(content, sections_to_remove=None):
    """
    Removes specified sections from the markdown content.
    """
    if sections_to_remove is None:
        sections_to_remove = ['acknowledgements', 'acknowledgments', 'references', 'bibliography', 
                             'works cited', 'citations', 'REFERENCES', 'BIBLIOGRAPHY']
    
    # Process YAML front matter if present
    if content.startswith('---'):
        end_yaml = content.find('---', 3)
        if end_yaml != -1:
            yaml_content = content[0:end_yaml+3]
            main_content = content[end_yaml+3:]
            
            # Remove acknowledgments from YAML
            for section in sections_to_remove:
                yaml_content = re.sub(rf'{section}:\s*\|.*?(?=\n\w+:|---)', 
                                     '', yaml_content, flags=re.IGNORECASE|re.DOTALL)
            
            content = yaml_content + main_content
    
    # Create patterns for standard headers (# Header)
    header_patterns = []
    for section in sections_to_remove:
        # Match headers like # Acknowledgments, ## References, etc.
        pattern = rf'(?:\n|^)(#{1,6}\s+{section}[^\n]*\n(?:(?!#{1,6}\s+)[^\n]*\n)*)'
        header_patterns.append(re.compile(pattern, re.IGNORECASE))
    
    # Create patterns for underlined headers (Header\n====== or Header\n-----)
    underline_patterns = []
    for section in sections_to_remove:
        # Match headers like "Acknowledgments\n============"
        pattern = rf'(?:\n|^)({section}[^\n]*\n[=\-]+\n(?:(?!#{1,6}\s+|[^\n]+\n[=\-]+\n)[^\n]*\n)*)'
        underline_patterns.append(re.compile(pattern, re.IGNORECASE))
    
    # Remove headers and their content
    for pattern in header_patterns + underline_patterns:
        content = pattern.sub('', content)
    
    return content

def process_markdown_document(input_file, output_file, clean_citations=True, 
                             remove_sections_list=None, skip_section_removal=False):
    """
    Main processing function that applies all cleaning operations.
    """
    # Read the file content
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Apply bracket and image cleaning
    if clean_citations:
        content = clean_brackets_and_images(content)
        print("Citation brackets and image references cleaned.")
    
    # Apply section removal
    if not skip_section_removal:
        content = remove_sections(content, remove_sections_list)
        print(f"Sections removed: acknowledgments, references, etc.")
    
    # Write the cleaned content
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Cleaning complete. Output saved to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Clean Markdown documents by removing citations and sections')
    parser.add_argument('input_file', help='Path to the input Markdown file')
    parser.add_argument('-o', '--output', help='Path to the output file (default: input_file_cleaned.md)')
    parser.add_argument('--no-clean-citations', action='store_true', help='Skip cleaning citation brackets')
    parser.add_argument('--no-remove-sections', action='store_true', help='Skip removing sections')
    parser.add_argument('-s', '--sections', nargs='+', 
                      help='Specific sections to remove (default: acknowledgments, references, etc.)')
    
    args = parser.parse_args()
    
    # Set default output filename if not provided
    if not args.output:
        base, ext = os.path.splitext(args.input_file)
        args.output = f"{base}_cleaned{ext}"
    
    # Process the document
    process_markdown_document(
        args.input_file,
        args.output,
        clean_citations=not args.no_clean_citations,
        remove_sections_list=args.sections,
        skip_section_removal=args.no_remove_sections
    )

if __name__ == "__main__":
    main()
