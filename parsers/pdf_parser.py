import pdfplumber

def extract_from_pdf_file(pdf_file_path):
    pdf_file = pdfplumber.open(pdf_file_path)
    text = ""
    for page in pdf_file.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    return text
