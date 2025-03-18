import os
import requests
import urllib.parse
import xml.etree.ElementTree as ET
import time
import hashlib
from pathlib import Path

def download_arxiv_papers(existing_folder, new_folder, search_term):
    # Create the new folder if it doesn't exist
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    
    # Get list of existing papers (by filename)
    existing_papers = set(os.listdir(existing_folder))
    
    # arXiv API endpoint
    base_url = "http://export.arxiv.org/api/query?"
    
    # Search parameters
    search_query = urllib.parse.quote(f'ti:"{search_term}"')
    start = 0
    max_results = 100
    
    # Construct the API query
    query = f"search_query={search_query}&start={start}&max_results={max_results}"
    
    # Make the API request
    response = requests.get(base_url + query)
    
    if response.status_code != 200:
        print(f"Error: API request failed with status code {response.status_code}")
        return
    
    # Parse the XML response
    root = ET.fromstring(response.content)
    
    # Define namespace
    namespace = {'arxiv': 'http://arxiv.org/schemas/atom'}
    
    # Process each entry (paper)
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip()
        
        # Check if "central configurations" is in the title (case insensitive)
        if "central configurations" not in title.lower():
            continue
        
        # Get the paper ID and PDF link
        id_url = entry.find('{http://www.w3.org/2005/Atom}id').text
        arxiv_id = id_url.split('/abs/')[-1]
        pdf_url = f"http://arxiv.org/pdf/{arxiv_id}.pdf"
        
        # Generate filename
        filename = f"{arxiv_id}.pdf"
        
        # Check if the paper already exists in the existing folder
        if filename in existing_papers:
            print(f"Skipping {filename} - already exists in {existing_folder}")
            continue
        
        # Download the PDF
        print(f"Downloading {filename}: {title}")
        try:
            pdf_response = requests.get(pdf_url)
            if pdf_response.status_code == 200:
                with open(os.path.join(new_folder, filename), 'wb') as f:
                    f.write(pdf_response.content)
                print(f"Successfully downloaded {filename}")
            else:
                print(f"Failed to download {filename}: HTTP {pdf_response.status_code}")
        except Exception as e:
            print(f"Error downloading {filename}: {e}")
        
        # Be nice to the arXiv API - don't make requests too quickly
        time.sleep(3)

# Specify your folders
existing_papers_folder = "/Users/rupakraut/Desktop/cc_LLM/cc_papers"
new_papers_folder = "/Users/rupakraut/Desktop/cc_LLM/cc_new_papers"
search_term = "central configurations"

# Run the function
download_arxiv_papers(existing_papers_folder, new_papers_folder, search_term)
