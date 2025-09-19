from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .extract import extract_text
from .analysis import analyze_text, translate_text
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Legal Simplifier API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Legal Simplifier API is running 🚀"}

@app.post("/analyze/")
async def analyze_document(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        text = extract_text(file.filename, contents)
        if not text:
            raise HTTPException(status_code=400, detail="Could not extract text from file.")
        result = analyze_text(text)
        return result
    except HTTPException:
        raise
    except Exception as e:
        logging.exception("Analyze error")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/translate/")
async def translate_endpoint(payload: dict):
    try:
        text = payload.get("text")
        target_language = payload.get("target_language")
        if not text or not target_language:
            raise HTTPException(status_code=400, detail="Missing text or target_language")
        translated = translate_text(text, target_language)
        return {"translated_text": translated}
    except HTTPException:
        raise
    except Exception as e:
        logging.exception("Translate error")
        raise HTTPException(status_code=500, detail=str(e))
