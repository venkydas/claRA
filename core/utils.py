import io
from typing import List
from PyPDF2 import PdfReader

async def pdf_to_text(file) -> str:
    # Reads file-like and returns all text
    reader = PdfReader(await file.read())
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()
