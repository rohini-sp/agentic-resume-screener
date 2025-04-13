# 🤖 Agentic Resume Screener using Gemini AI

A multi-agent AI system built with **Streamlit** and **Gemini Flash API** that intelligently analyzes resumes and evaluates them against a job description. The system simulates **three functional agents** to create a transparent, structured, and explainable evaluation flow.

---

## 🧠 Agentic AI Workflow

### 👤 Agent 1: Resume Extractor
- Extracts structured candidate data (skills, experience, education) from PDF or DOCX resumes using:
  - `pdfplumber` for PDFs
  - `python-docx` for Word documents
- Uses **Gemini AI** to transform raw text into structured information.

### 🎯 Agent 2: Matcher
- Evaluates how well the resume aligns with the job description.
- Uses Gemini to generate a **match score (out of 100)** and highlight key matching areas.

### 💬 Agent 3: Explainer
- Converts the match analysis into a **plain-language summary**.
- Designed for recruiters and hiring teams to quickly understand fit.

---

## 🖥️ Features

- Upload **multiple resumes** (.pdf or .docx)
- Paste a **job description**
- Receive:
  - Candidate details
  - Match score & analysis
  - HR-friendly explanation

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-username/agentic-resume-screener.git
cd agentic-resume-screener
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your Gemini API Key

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

> Don’t have a key? Sign up at [Google AI Studio](https://makersuite.google.com/app) to get one.

### 4. Launch the Streamlit App

```bash
streamlit run app.py
```

---

## 🧩 Tech Stack

- **Streamlit** — interactive web UI
- **Gemini 1.5 Flash API** — for all AI prompts
- **pdfplumber** — for parsing PDF resumes
- **python-docx** — for parsing Word resumes
- **dotenv** — for secure API key handling

---

## 📂 Project Structure

```
agentic-resume-screener/
├── app.py                # Streamlit app
├── .env                  # Your Gemini API key (not committed)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 📌 Sample Use Cases

- Screening candidates for job openings
- Automating shortlisting in HR workflows
- Educational tools for career guidance

---

## 🧠 Agentic AI Design

This project uses an **agentic AI paradigm**:
- Modular, role-based architecture
- Better explainability and clarity in outputs
- Easily extensible to include new agents (e.g., feedback generator, bias checker)

---

## 🙌 Contributing

PRs and suggestions are welcome! To contribute:
1. Fork the repo
2. Make your changes
3. Submit a pull request

---

Built with ❤️ and Gemini AI to simplify hiring.