from fastapi import FastAPI, UploadFile
from main import resume_parser_pdf, resume_parser_docx

api_app = FastAPI()

async def parse(file: UploadFile):
    path = "uploaded.pdf"
    File = open(path, "wb")
    File.write(await file.read())

    return resume_parser_pdf(path)

