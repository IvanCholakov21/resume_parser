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



def extract_phone_number(text):
    pattern = (
        r"(\+\d{1,3}\s?)?"
        r"(\(?\d{3}\)?[\s-]?)"
        r"\d{3}[\s-]?"
        r"\d{4}"
    )
    match = re.search(pattern, text)
    if match:
        return match.group()
    else:
        return None


def extract_birthday(text):
    pattern = r"""
    ^(?:
        (31[\/\.-](0?[13578]|1[02])[\/\.-](19|20)\d{2}) |
        (30[\/\.-](0?[469]|11)[\/\.-](19|20)\d{2}) |
        ((0?[1-9]|1\d|2[0-8])[\/\.-](0?2)[\/\.-](19|20)\d{2}) |
        (29[\/\.-]0?2[\/\.-]((19|20)(04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)))
    )$
    """

    regex = re.compile(pattern, re.VERBOSE)

    match = re.search(regex, text)
    if match:
        return match.group()
    else:
        return None
