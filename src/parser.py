"""
ClawdBot Action Assistant - Phase 1: File Handling & Parsing
------------------------------------------------------------
This script is responsible for:
1. Ingesting CV files in PDF and DOCX formats.
2. Extracting raw text from these files.
3. Performing basic text cleaning (normalizing spaces, removing extra newlines).
4. Preparing the raw text for the next phase of analysis.

"""
import fitz  # To work with PDF files
import docx  # To work with Word documents
import re    # To search for text patterns
import os
import sys

def extract_from_pdf(path):
    """Extracts raw text from a PDF file."""
    text = ""
    try:
        with fitz.open(path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

def extract_from_docx(path):
    """Extracts raw text from a DOCX file."""
    try:
        doc = docx.Document(path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"Error reading DOCX: {e}"

def clean_text(text):
    """Normalizes spacing and removes extra newlines."""
    cleaned = re.sub(r'\s+', ' ', text).strip()
    return cleaned

def save_raw_text(text, original_path):
    """Stores the cleaned text into a .txt file in the data/ directory."""
    # Ensure the data directory exists
    if not os.path.exists("data"):
        os.makedirs("data")

    base_name = os.path.basename(original_path)
    file_name_without_ext = os.path.splitext(base_name)[0]
    output_path = os.path.join("data", f"extracted_{file_name_without_ext}.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path


if __name__ == "__main__":
    print("--- ClawdBot File Ingestion Module Started ---")

    # Check if a file path was provided via terminal
    if len(sys.argv) < 2:
        print("Usage: python3 src/parser.py <path_to_cv_file>")
        sys.exit(1)

    file_to_process = sys.argv[1]


if os.path.exists(file_to_process):
        # 1. Ingestion & Extraction
        if file_to_process.lower().endswith(".pdf"):
            raw_content = extract_from_pdf(file_to_process)
            print(f"Status: PDF detected -> {file_to_process}")
        elif file_to_process.lower().endswith(".docx"):
            raw_content = extract_from_docx(file_to_process)
            print(f"Status: DOCX detected -> {file_to_process}")
        else:
            print("Status: Unsupported file format.")
            raw_content = ""

        if raw_content and len(raw_content.strip()) > 0 and not raw_content.startswith("Error"):
            # 2. Cleaning
            cleaned_content = clean_text(raw_content)
            # 3. Storage
            saved_path = save_raw_text(cleaned_content, file_to_process)
            print(f"Success: Text extracted and saved at: {saved_path}")
        else:
            print("Notice: No text could be extracted or file is invalid.")
    else:
        print(f"Error: File not found at {file_to_process}")
