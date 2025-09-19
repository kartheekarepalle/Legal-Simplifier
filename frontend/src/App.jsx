import React, { useState, useRef } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");
  const [risks, setRisks] = useState([]);
  const [translated, setTranslated] = useState("");
  const [targetLang, setTargetLang] = useState("en");
  const [loading, setLoading] = useState(false);
  const inputRef = useRef(null);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setSummary("");
      setRisks([]);
      setTranslated("");
    }
  };

  const handleUploadClick = () => {
    inputRef.current.click();
  };

  const handleAnalyze = async () => {
    if (!file) return alert("Please select a file first!");
    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://127.0.0.1:8000/analyze/", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      setSummary(data.summary || "");
      setRisks(data.risks || []);
    } catch (err) {
      console.error(err);
      alert("Error analyzing file");
    }
    setLoading(false);
  };

  const handleTranslate = async () => {
    if (!summary) return alert("No summary to translate");
    try {
      const res = await fetch("http://127.0.0.1:8000/translate/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: summary, target_language: targetLang }),
      });
      const data = await res.json();
      setTranslated(data.translated_text || "");
    } catch (err) {
      console.error(err);
      alert("Error translating text");
    }
  };

  const toggleTheme = () => {
    document.body.classList.toggle("light-mode");
  };

  // 🔹 Helper to add icons for risks
  const getRiskIcon = (risk) => {
    const lower = risk.toLowerCase();
    if (lower.includes("high")) return "🚨";
    if (lower.includes("medium")) return "⚠️";
    if (lower.includes("low")) return "ℹ️";
    return "⚠️";
  };

  return (
    <div className="app-container">
      <button className="theme-toggle" onClick={toggleTheme}>
        Toggle Theme
      </button>

      <div className="header">
        <div className="logo">⚖ LegalSimplifier </div>
        <div className="tagline">Simplify complex legal documents in seconds. </div>
      </div>

      <div className="upload-card" onClick={handleUploadClick}>
        <input
          type="file"
          ref={inputRef}
          style={{ display: "none" }}
          onChange={handleFileChange}
        />
        {!file && (
          <div className="placeholder-text">
            <div className="upload-icon">📄</div>
            <p>Click to upload your file</p>
          </div>
        )}
        {file && (
          <div className="file-info">
            <div className="file-name">{file.name}</div>
            <button className="reset-button" onClick={() => setFile(null)}>
              ✖
            </button>
          </div>
        )}
      </div>

      <button
        className="analyze-button"
        onClick={handleAnalyze}
        disabled={loading || !file}
      >
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {summary && (
        <div className="summary-card">
          <div className="summary-card-title">Summary</div>
          <p>{summary}</p>
        </div>
      )}

      {/* 🔹 Risks Card (always visible if summary exists) */}
      {summary && (
        <div className="risks-card">
          <div className="summary-card-title">Risks Detected</div>
          <ul>
            {risks.length > 0 ? (
              risks.map((r, idx) => (
                <li key={idx}>
                  {getRiskIcon(r)} {r}
                </li>
              ))
            ) : (
              <li>✅ No risks found</li>
            )}
          </ul>
        </div>
      )}

      {summary && (
        <div style={{ marginTop: "1rem", textAlign: "center" }}>
          <select
            value={targetLang}
            onChange={(e) => setTargetLang(e.target.value)}
            style={{
              marginRight: "0.5rem",
              padding: "0.5rem",
              borderRadius: "5px",
            }}
          >
            <option value="en">English</option>
            <option value="hi">Hindi</option>
            <option value="te">Telugu</option>
            <option value="ta">Tamil</option>
            <option value="bn">Bengali</option>
            <option value="mr">Marathi</option>
          </select>
          <button onClick={handleTranslate} className="analyze-button">
            Translate Summary
          </button>
        </div>
      )}

      {translated && (
        <div className="summary-card" style={{ marginTop: "1rem" }}>
          <div className="summary-card-title">Translated Summary</div>
          <p>{translated}</p>
        </div>
      )}
    </div>
  );
}

export default App;
