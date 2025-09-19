import re
from collections import Counter
from deep_translator import GoogleTranslator

# Risk keywords + explanations
RISK_DICT = {
    "termination": "This clause allows the company to terminate your employment under certain conditions.",
    "probation": "Indicates a probation period where your performance is evaluated before confirmation.",
    "non-compete": "Restricts you from joining competitors after leaving the company.",
    "confidentiality": "You must keep company information private, even after leaving.",
    "notice period": "Specifies how long you must give notice before leaving the job.",
    "salary deduction": "Certain deductions may be applied under specific circumstances.",
    "penalty": "Mentions penalties or fines.",
    "liability": "Describes liability or responsibility clauses."
}

# Small stopword set to make summary better (keeps it light)
STOPWORDS = {
    "the","and","is","in","it","of","to","a","for","on","that","this","with","as","are","be","by","or",
    "an","at","from","was","were","which","has","have","had","but","not","will","can","may","such"
}

def _split_sentences(text: str):
    # crude sentence splitter (works well enough for most docs)
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip() for s in sentences if len(s.strip()) > 10]

def summarize_text(text: str, max_sentences: int = 6) -> str:
    if not text or len(text.strip()) < 200:
        return text.strip()

    sentences = _split_sentences(text)
    if len(sentences) <= max_sentences:
        return " ".join(sentences).strip()

    words = re.findall(r'\w+', text.lower())
    words = [w for w in words if w not in STOPWORDS and len(w) > 1]
    if not words:
        return " ".join(sentences[:max_sentences]).strip()

    freq = Counter(words)
    max_freq = max(freq.values()) if freq else 1
    for k in list(freq.keys()):
        freq[k] = freq[k] / max_freq

    sentence_scores = []
    for i, s in enumerate(sentences):
        s_words = re.findall(r'\w+', s.lower())
        score = sum(freq.get(w, 0) for w in s_words)
        denom = max(len(s_words), 1)
        sentence_scores.append((i, score / denom, s))

    sentence_scores_sorted = sorted(sentence_scores, key=lambda x: x[1], reverse=True)
    top = sorted(sentence_scores_sorted[:max_sentences], key=lambda x: x[0])
    summary = " ".join([s for (_, _, s) in top]).strip()
    return summary or " ".join(sentences[:max_sentences]).strip()

def detect_risks(text: str):
    found = []
    text_lower = text.lower()
    for kw, expl in RISK_DICT.items():
        if kw.lower() in text_lower:
            found.append(f"{kw}: {expl}")
    return found

def translate_text(text: str, target_language: str) -> str:
    if not text:
        return ""
    try:
        translator = GoogleTranslator(source='auto', target=target_language)
        translated = translator.translate(text)
        return translated
    except Exception as e:
        return f"Translation failed: {e}"

def analyze_text(text: str):
    if not text or not text.strip():
        return {"summary": "", "risks": ["No text extracted from the document"]}

    summary = summarize_text(text, max_sentences=6)
    risks = detect_risks(text)
    if not risks:
        risks = ["No major risks detected"]

    return {"summary": summary, "risks": risks}
