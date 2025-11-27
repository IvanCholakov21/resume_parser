from docx import Document

def extract_text_from_docx(doc_file_path):
    document = Document(doc_file_path)

    text = "\n".join([p.text for p in document.paragraphs])
    return text


