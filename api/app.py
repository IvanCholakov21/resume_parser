from fastapi import FastAPI, UploadFile, File, HTTPException
from main import resume_parser_pdf, resume_parser_docx
import os

the_api = FastAPI()
@the_api.post("/parse")
async def parse_pdf(file: UploadFile = File(...)):

    filename = file.filename.lower()

    if filename.endswith(".pdf"):

        save_name = "uploaded.pdf"
        parser = resume_parser_pdf

    elif filename.endswith(".docx"):

        save_name = "uploaded.docx"
        parser = resume_parser_docx

    else:
        raise HTTPException(status_code=400, detail="Invalid file type. Parser only supports PDF and DOCX files.")

    with open(save_name, "wb") as f:
        f.write(await file.read())

    return parser(save_name)

