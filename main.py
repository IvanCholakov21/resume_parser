import json

from nlp.extractor import extract_name, extract_email
from parsers.pdf_parser import extract_from_pdf_file
from parsers.doc_parser import extract_text_from_docx


def resume_parser_pdf(resume_file):
    text = extract_from_pdf_file(resume_file)

    data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "raw_text": text

    }

    return json.dump(data, indent=4)


def resume_parser_docx(resume_file):
    text = extract_text_from_docx(resume_file)

    data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "raw_text": text
    }

    return json.dump(data, indent=4)


if __name__ == "__main__":
    print(resume_parser_pdf("examples/resume.pdf"))