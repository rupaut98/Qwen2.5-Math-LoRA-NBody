import re

def clean_markdown_document(input_file, output_file):
    # Read the markdown file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Pattern 1: Remove [X] where X contains only alphanumeric characters
    # But keep those containing symbols like [\times] or [0, \pi / 4]
    pattern1 = r'\[[a-zA-Z0-9\s,]+\]'
    content = re.sub(pattern1, '', content)
    
    # Pattern 2: Remove image references like ![img-15.jpeg](img-15.jpeg)
    pattern2 = r'!\[img-\d+\.jpeg\]\(img-\d+\.jpeg\)'
    content = re.sub(pattern2, '', content)
    
    # Write the cleaned content to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Cleaning complete. Output saved to {output_file}")

# Usage
input_file = '/Users/rupakraut/Desktop/cc_LLM/cc_preprocess/cleaned_central_configurations_corpus.md'
output_file = 'cleaned_central_configurations_corpus.md'
clean_markdown_document(input_file, output_file)
