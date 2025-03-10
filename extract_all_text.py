import os
import json
import time
from pathlib import Path
from mistralai import Mistral
import os

# Initialize the Mistral client with your API key
api_key = os.getenv("MISTRAL_API_KEY") # You should use environment variables for sensitive keys in production
client = Mistral(api_key=api_key)

# Path to the directory containing PDF files
pdf_directory = "/Users/rupakraut/Desktop/cc_LLM/cc_papers"

# Create the directory if it doesn't exist
os.makedirs(pdf_directory, exist_ok=True)

# Output file for the combined corpus
corpus_file = "central_configurations_corpus.md"

# Process all PDFs and extract text
def process_pdfs_in_directory(directory, output_file):
    pdf_files = [f for f in os.listdir(directory) if f.lower().endswith('.pdf')]
    
    # Create or clear the output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Central Configurations Corpus\n\n")
    
    print(f"Found {len(pdf_files)} PDF files to process.")
    
    for index, pdf_file in enumerate(pdf_files, 1):
        pdf_path = os.path.join(directory, pdf_file)
        paper_name = os.path.splitext(pdf_file)[0]
        
        print(f"Processing file {index}/{len(pdf_files)}: {pdf_file}")
        
        try:
            # Extract text from the current PDF
            markdown_content = extract_text_from_pdf(pdf_path, paper_name)
            
            # Append the extracted text to the corpus file
            with open(output_file, "a", encoding="utf-8") as f:
                f.write(f"\n\n## {paper_name}\n\n")
                f.write(markdown_content)
                f.write("\n\n---\n\n")  # Add a separator between papers
                
            print(f"✓ Added content from {pdf_file} to corpus")
            
        except Exception as e:
            print(f"× Error processing {pdf_file}: {str(e)}")
        
        # Add a small delay between API calls to avoid rate limiting
        if index < len(pdf_files):
            time.sleep(2)
    
    print(f"Processing complete. All content saved to {output_file}")

# Function to extract text from a single PDF
def extract_text_from_pdf(pdf_path, paper_name):
    # Upload the PDF
    with open(pdf_path, "rb") as pdf_file:
        uploaded_pdf = client.files.upload(
            file={"file_name": os.path.basename(pdf_path), "content": pdf_file},
            purpose="ocr"
        )
    
    print(f"  Uploaded {paper_name}, File ID: {uploaded_pdf.id}")
    
    # Get signed URL
    signed_url = client.files.get_signed_url(file_id=uploaded_pdf.id)
    
    # Process with OCR
    ocr_response = client.ocr.process(
        model="mistral-ocr-latest",
        document={
            "type": "document_url",
            "document_url": signed_url.url,
        }
    )
    
    # Extract text from all pages
    pages = ocr_response.pages or []
    all_text = ""
    
    for page in pages:
        all_text += page.markdown + "\n\n"
    
    return all_text

# Run the extraction process
process_pdfs_in_directory(pdf_directory, corpus_file)
