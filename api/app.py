from fastapi import FastAPI, UploadFile, File, HTTPException
from main import resume_parser_pdf, resume_parser_docx
import os

the_api = FastAPI()
@the_api.post("/parse")
async def parse_pdf(file: UploadFile = File(...)):

    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        parser = resume_parser_pdf(file)
        save_name = "uploaded.pdf"

    elif filename.endswith(".docx"):
        parser = resume_parser_docx(file)
        save_name = "uploaded.docx"

    else:
        raise HTTPException(status_code=400, detail="Invalid file type. Parser only supports PDF and DOCX files.")

    async with open(save_name, "wb") as file:
        content = await file.read()
        await file.write(content)

    return parser(save_name)

