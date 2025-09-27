# ⚖️ Legal-Simplifier

**A Full-Stack Application** for Summarizing and Clarifying Complex Legal Documents.

---

## 🧩 Problem Statement

Legal-Simplifier is an intelligent tool designed to make complex legal and technical documents accessible to everyone. Built with a React frontend and a FastAPI (Python) backend, the application allows users to upload various document types (PDF, DOCX, TXT) and receive a concise, easy-to-understand summary.

---

## ✨ Features

Multi-Format Upload: Supports PDF, DOCX, TXT, and Excel file uploads.

Intelligent Summarization: Uses a Python backend to process documents and generate clear, simplified summaries.

Intuitive UI: A clean and modern user interface built with React.

Full-Stack Architecture: Separated frontend and backend for scalable development.

Translation: Summary is also be Translated in different Languages.

---

## 🎥 Demo:

🔗 Project Links
GitHub Repository: https://github.com/kartheekarepalle/Legal-Simplifier

Demo: https://github.com/kartheekarepalle/Legal-Simplifier/blob/main/simplifier-demo.mp4

---

## 🏗️ Project Architecture

```
Legal-Simplifier/
├── backend/                  # The Python/FastAPI API server
│   ├── main.py               # FastAPI application entry point
│   └── requirements.txt      # Python dependencies for the backend.
│
├── frontend/                 # The React application built with Vite
│   ├── public/               # Static assets
│   ├── src/                  # React source files, components, and pages
│   └── package.json          # JavaScript dependencies.
│
├── .gitattributes            # LFS configuration (for large files)
├── .gitignore
├── LICENSE                   # MIT License
├── package.json              # Root-level JavaScript configs (if used)
├── requirements.txt          # Shared Python dependencies (if used)
├── simplifier-demo.mp4       # The large file you previously committed (LFS placeholder)
└── vercel.json               # Configuration for Vercel deployment
```

---

## 🚀 Getting Started

### Follow these steps to set up and run the project locally.

You must have the following installed:

React and Vite

Python 3.10+

[npm] or [yarn]

### 1. Clone the Repository 📂

```bash
git clone https://github.com/kartheekarepalle/Legal-Simplifier.git
cd Legal-Simplifier
```

### 2. Backend Setup (FastAPI/Python) 🐍
This section installs Python dependencies and starts the API server.

```bash
# Navigate to the backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Start the FastAPI server (it will run on http://localhost:8000 by default)
uvicorn main:app --reload
```

### 3. Frontend Setup (React/Vite) ⚛️
Open a new, separate terminal window and follow these steps to install JavaScript dependencies and start the React development server.

```bash
# Navigate back to the project root, then into the frontend directory
cd Legal-Simplifier
cd frontend

# Install Node.js dependencies
npm install

# Start the React development server (it will run on http://localhost:5173 by default)
npm run dev
```

---

---

## 🛠️ Tech Stack

<p align="center">
<img src="https://skillicons.dev/icons?i=vite,react,javascript,css,python,fastapi,npm,vercel,github" />
</p>

```bash
⚡ Vite: Frontend tooling and build speed.
⚛️ React: Building the user interface (UI).
📜 JavaScript: Frontend logic and user interactivity.
🎨 CSS: Styling and layout design.
🐍 Python: Backend processing and scripting.
🚀 FastAPI: Creating the high-performance API endpoints.
📦 npm: Managing JavaScript dependencies.
```

---

## ⚙️ Deployment
This project is configured as a Monorepo on Vercel. The deployment process is managed by the vercel.json file at the root of the repository.

---

## 🤝 Contribution
Contributions are welcome! If you have suggestions for features, bug fixes, or improvements, please: Fork the repository.

---

## 📄 License
Distributed under the MIT License. See LICENSE.md for more information.

---

## 🙌 Acknowledgements
Inspired by the need for simplified access to legal information.

Built with the support of the open-source community.

Linkedin: https://www.linkedin.com/in/kartheeka-repalle-2139a1363/
