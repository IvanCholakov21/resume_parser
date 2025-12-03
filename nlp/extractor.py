import json

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


def extract_experience(text):
    nlp = spacy.load('en_core_web_sm')

    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    entries_experience = []
    date_pattern = r"(\b\d{4}\b|\bJan|\bFeb|\bMar|\bApr|\bMay|\bJun|\bJul|\bAug|\bSep|\bOct|\bNov|\bDec)"
    document = nlp(text)
    for sent in document.sents:
        sent_text = sent.text.strip()

        companies = []
        dates = []
        job_title_candidates = []

        for ent in sent.ents:
            if ent.label_ == "ORG":
                companies.append(ent.text)

        dates = re.findall(date_pattern, sent_text)


        for chunk in sent.noun_chunks:
           if any(keyword in chunk.text.lower() for keyword in ["engineer", "developer", "manager", "analyst", "designer","support","coordinator",""]):
               job_title_candidates.append(chunk.text)


        if companies or dates or job_title_candidates:
            entries_experience.append({
                "job_title": job_title_candidates[0] if job_title_candidates else None,
                "company": companies[0] if companies else None,
                "start_date": dates[0] if len(dates) > 0 else None,
                "end_date": dates[1] if len(dates) > 1 else None
            })

    return entries_experience


with open("Database/countries.json","r", encoding="utf-8") as file:
    countries_data = json.load(file)

with open("Database/cities.json","r", encoding="utf-8") as file:
    cities_data = json.load(file)

with open("Database/postal_codes.json","r", encoding="utf-8") as file:
    postal_codes_data = json.load(file)


countries = set([c.lower() for c in countries_data["countries"]])
cities = set([c.lower() for c in cities_data["cities"]])
aliases = {k.lower(): v for k, v in countries_data["aliases"].items()}


def extract_location(text):
    document = nlp(text)

    for ent in document.ents:
        if ent.label_ == "GPE" or ent.label_ == "LOC":
            return classify_location(ent.text)



    return None

def classify_location(text):
    entry = {
        "city": None,
        "ZIP": None,
        "Country": None,
    }

    check = text.strip()


    if check.lower() in cities:
        entry["city"] = text


    if check.lower() in countries or check.lower() in aliases:
        entry["Country"] = text


    postal_patterns = postal_codes_data["patterns"]

    for country_name, pattern in postal_patterns.items():
        if re.match(pattern, check):
            entry["ZIP"] = text
            if not entry["Country"]:
                entry["Country"] = country_name


    return entry




