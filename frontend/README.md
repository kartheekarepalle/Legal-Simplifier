⚖️ Legal Simplifier
---

Legal Simplifier is a full-stack web application designed to demystify complex legal documents. By transforming dense legal jargon into plain, easy-to-understand language, it aims to enhance clarity and access to critical information for everyone.

🧩 Problem Statement
---
Legal documents are often dense and full of technical terminology, making them difficult for the average person to comprehend. This barrier prevents people from fully understanding their rights and obligations. This project seeks to bridge the gap between legal and public understanding.

🔍 What It Does
---
Accepts Legal Documents: Allows users to upload or paste legal text via a user-friendly interface.

Simplifies Text: The backend processes the text, identifying and simplifying complex phrases.

Delivers a Clean UI: The frontend is built using React and Vite for a modern and responsive user experience.

Runs Concurrently: Uses concurrently to manage both the frontend and backend servers with a single command.

🎥 Demo:
---
🔗 Project Links
GitHub Repository: https://github.com/kartheekarepalle/Legal-Simplifier

Live Demo: https://Legal-Simplifier.vercel.app

🏗️ Project Architecture
---
Legal-Simplifier/
│
├── frontend/                   # Frontend code (React + Vite)
│   ├── src/                    # Source files
│   ├── public/                 # Static assets
│   └── package.json            # Frontend dependencies
│
├── backend/                    # Backend code (Node.js + Express)
│   ├── app.js                  # Main server file
│   └── package.json            # Backend dependencies
│
├── package.json                # Main project dependencies
├── README.md                   # This file
└── .gitignore                  # Git ignore file

🚀 Getting Started
---
Follow these steps to set up and run the project locally.

1. Clone the Repository
Bash

git clone https://github.com/kartheekarepalle/Legal-Simplifier.git
cd Legal-Simplifier
2. Install Dependencies
Bash

Install root dependencies
npm install concurrently express

# Navigate to frontend and install dependencies
cd frontend
npm install

# Return to root directory
cd ..
3. Run the Application
With all dependencies installed, you can start both the frontend and backend with a single command from the project's root directory.

Bash

npm run dev
The application will be accessible via a local URL (e.g., http://localhost:5173) in your browser.

📦 Tech Stack
---
Core Technologies:
<p align="center">
<img src="https://skillicons.dev/icons?i=react,vite,nodejs,express,npm,git" />
</p>

📄 License
---
This project is licensed under the MIT License.
See the LICENSE file for more details.

🙌 Acknowledgements
---
Inspired by the need for simplified access to legal information.

Built with the support of the open-source community.