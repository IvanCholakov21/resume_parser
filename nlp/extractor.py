import spacy
import re


nlp = spacy.load('en_core_web_sm')


def extract_name(text):
    document = nlp(text)


    for ent in document.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return None


def extract_email(text):
    match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    if match:
        return match.group()
    else:
        return None

    