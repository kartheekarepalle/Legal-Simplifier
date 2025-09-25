from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.extract import extract_text
from backend.analysis import analyze_text, translate_text
from mangum import Mangum
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Legal Simplifier API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with your frontend domain for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Legal Simplifier API is running 🚀"}

# 🔹 Updated route to match frontend fetch
@app.post("/api/analyze/")
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

# 🔹 Updated route to match frontend fetch
@app.post("/api/translate/")
async def translate_endpoint(request: Request):
    try:
        payload = await request.json()
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

handler = Mangum(app)
