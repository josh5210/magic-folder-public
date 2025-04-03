import os, shutil
from classifier import categorize_text
from docx_parsing import extract_text_from_docx
from mover import move_and_rename
from pdf_parsing import extract_text_from_pdf


def process_file(file_path):
    # 1-Determine file type by extension
    ext = os.path.splitext(file_path)[1].lower()
    if ext in ['.txt', '.md']:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
    elif ext == '.pdf':
        text = extract_text_from_pdf(file_path)
    elif ext in ['.docx', '.doc']:
        text = extract_text_from_docx(file_path)
    else:
        text = None  # unsupported type for text extraction
    
    if not text or text.strip() == "":
        print(f"No text extracted from {file_path}. Skipping categorization.")
        # Either move it to an "Unsorted" folder or return here.
        return
    
    # 2-Analyze text with AI to get a category
    category = categorize_text(text)
    # 3-Move (and possibly rename) the file to the category folder
    move_and_rename(file_path, category)
