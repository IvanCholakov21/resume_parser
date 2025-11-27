import pdfplumber

def extract_from_pdf_file(pdf_file_path):
    pdf_file = pdfplumber.open(pdf_file_path)
    text = ""
    for page in pdf_file:
        text += page.extract_text() + "\n"

    return text
