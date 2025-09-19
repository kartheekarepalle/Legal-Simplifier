# backend/extract.py
import io
import os
import pandas as pd
from PyPDF2 import PdfReader
from docx import Document
import docx2txt
from pptx import Presentation


def extract_text(filename: str, file_contents: bytes) -> str:
    extension = filename.split(".")[-1].lower()
    try:
        # ----- PDF -----
        if extension == "pdf":
            reader = PdfReader(io.BytesIO(file_contents))
            return "\n".join([p.extract_text() or "" for p in reader.pages]).strip()

        # ----- DOCX -----
        if extension == "docx":
            try:
                doc = Document(io.BytesIO(file_contents))
                return "\n".join(para.text for para in doc.paragraphs).strip()
            except Exception:
                return docx2txt.process(io.BytesIO(file_contents))

        # ----- TXT -----
        if extension == "txt":
            return file_contents.decode("utf-8", errors="ignore").strip()

        # ----- PPTX -----
        if extension == "pptx":
            prs = Presentation(io.BytesIO(file_contents))
            slides_text = []
            for slide in prs.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "text"):
                        slides_text.append(shape.text)
            return "\n".join(slides_text).strip()

        # ----- Excel (XLSX / XLS) -----
        if extension in ["xlsx", "xls"]:
            excel_data = pd.read_excel(io.BytesIO(file_contents), sheet_name=None)
            text = []
            for sheet_name, df in excel_data.items():
                text.append(f"Sheet: {sheet_name}")
                text.append(df.astype(str).apply(lambda x: " ".join(x), axis=1).str.cat(sep="\n"))
            return "\n".join(text).strip()

        # ----- CSV -----
        if extension == "csv":
            df = pd.read_csv(io.BytesIO(file_contents))
            return df.astype(str).apply(lambda x: " ".join(x), axis=1).str.cat(sep="\n")

        # ----- Unsupported -----
        return f"⚠️ Sorry, {extension.upper()} files are not fully supported yet."

    except Exception as e:
        print(f"Extraction failed for {filename}: {e}")
        return "❌ Could not extract text from this file."
