

from nlp.extractor import *
from parsers.pdf_parser import extract_from_pdf_file
from parsers.doc_parser import extract_text_from_docx


def resume_parser_pdf(resume_file):
    text = extract_from_pdf_file(resume_file)

    data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone_number(text),
        "birthday": extract_birthday(text),
        "experience": extract_experience(text),
        "location": extract_location(text),
        "raw_text": text

    }

    return data


def resume_parser_docx(resume_file):
    text = extract_text_from_docx(resume_file)

    data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone_number(text),
        "birthday": extract_birthday(text),
        "experience": extract_experience(text),
        "location": extract_location(text),

        "raw_text": text
    }

    return data


if __name__ == "__main__":
    print(resume_parser_pdf("examples/resume.pdf"))