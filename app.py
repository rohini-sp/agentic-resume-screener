import os
import streamlit as st
import pdfplumber
import docx
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ==== Extract Resume Text ====
def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([p.extract_text() or "" for p in pdf.pages])

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def get_resume_text(uploaded_file):
    if uploaded_file.name.endswith('.pdf'):
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith('.docx'):
        return extract_text_from_docx(uploaded_file)
    else:
        return "Unsupported file format."

# ==== Gemini Calls ====
def gemini_prompt(system_prompt, user_input):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([{"role": "user", "parts": [system_prompt + "\n" + user_input]}])
    return response.text

# ==== Agentic Flow ====
def agentic_resume_screening(resume_text, job_description):
    # Agent 1: Extractor
    info = gemini_prompt("You are a resume parser. Extract structured candidate details like skills, experience, education, etc.", resume_text)

    # Agent 2: Matcher
    match = gemini_prompt("You are a recruiter. Match the resume to the job description and output score out of 100 & key matches.", f"Resume Info:\n{info}\n\nJob Description:\n{job_description}")

    # Agent 3: Explainer
    explain = gemini_prompt("You are an HR assistant. Summarize the matching in plain language (3-5 sentences).", match)

    return info, match, explain

# ==== Streamlit App ====
st.set_page_config(page_title="Agentic Resume Screener", layout="wide")
st.title("🤖 Agentic Resume Screener using Gemini AI")

st.markdown("""
Upload one or more resumes (PDF/DOCX) and provide a job description.
The app will extract info, match them, and explain it in simple terms using **multi-agent AI** powered by **Gemini**.
""")

job_description = st.text_area("📋 Paste Job Description", height=200)

uploaded_resumes = st.file_uploader("📂 Upload Resume(s) - PDF or DOCX", type=["pdf", "docx"], accept_multiple_files=True)

if st.button("🔍 Analyze Resumes"):
    if not job_description or not uploaded_resumes:
        st.warning("Please upload resumes and provide a job description.")
    else:
        for file in uploaded_resumes:
            st.subheader(f"📄 {file.name}")

            resume_text = get_resume_text(file)
            with st.spinner("🧠 Running AI Agents..."):
                extracted_info, match_report, explanation = agentic_resume_screening(resume_text, job_description)

            with st.expander("🕵️ Extracted Info"):
                st.text(extracted_info)

            with st.expander("🎯 Match Report"):
                st.text(match_report)

            with st.expander("💬 HR-Friendly Explanation"):
                st.write(explanation)
