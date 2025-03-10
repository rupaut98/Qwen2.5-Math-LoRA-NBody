import re
import argparse
import os

def remove_markdown_sections(input_file, output_file, sections_to_remove=None):
    """
    Removes specified sections from a Markdown file.
    
    Args:
        input_file: Path to the input Markdown file
        output_file: Path for the cleaned output file
        sections_to_remove: List of section names to remove (case-insensitive)
    """
    if sections_to_remove is None:
        sections_to_remove = ['acknowledgements', 'acknowledgments', 'references', 'bibliography', 
                             'works cited', 'citations', 'Acknowledgements', 'Acknowledgments', 'References', 'Bibliography', 
                             'Works cited', 'Citations', "REFERENCES", "BIBLIOGRAPHY"]
    
    # Read the file content
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
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
    
    # Write the cleaned content
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Sections removed: {', '.join(sections_to_remove)}")
    print(f"Cleaned document saved to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Remove acknowledgments and references sections from Markdown files')
    parser.add_argument('input_file', help='Path to the input Markdown file')
    parser.add_argument('-o', '--output', help='Path to the output file (default: input_file_cleaned.md)')
    parser.add_argument('-s', '--sections', nargs='+', 
                      help='Specific sections to remove (default: acknowledgements, references, bibliography, etc.)')
    
    args = parser.parse_args()
    
    # Set default output filename if not provided
    if not args.output:
        base, ext = os.path.splitext(args.input_file)
        args.output = f"{base}_cleaned{ext}"
    
    remove_markdown_sections(args.input_file, args.output, args.sections)

if __name__ == "__main__":
    main()
