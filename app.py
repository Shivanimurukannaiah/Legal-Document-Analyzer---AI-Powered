# app.py

import streamlit as st
from PyPDF2 import PdfReader
import docx
import openai
import re

# ----------- OPENAI SETUP -----------
openai.api_key = "api key"  # 🔐 Replace with your real key

def analyze_with_openai(text):
    prompt = f"""
You are a legal assistant AI. Analyze the following legal or official document and provide:

## Questions and Answers
List all questions (explicit or implied) and provide clear, concise answers based on the document.

## Consequences of Signing
Describe the potential legal or practical consequences if someone signs this document.

## Subtopics
Break down the document into 3–7 subtopics with short summaries.

Document:
{text}
"""

    # This is the new API call syntax for v1.0.0+
    response = openai.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        prompt=prompt,
        temperature=0.4,
        max_tokens=500  # Add max_tokens to limit response length
    )

    # Return the AI response
    return response['choices'][0]['text'].strip()  # Adjusted for new response format

# ----------- TEXT EXTRACTORS -----------
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    return "\n".join([page.extract_text() or "" for page in reader.pages])

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_txt(file):
    return file.read().decode("utf-8")

# ----------- STREAMLIT UI -----------
st.set_page_config(page_title="Legal Document Analyzer", layout="wide")
st.title("📄 Legal Document Analyzer - AI Powered by OpenAI")

# Create two columns for layout
col1, col2 = st.columns([3, 1])  # Left column (wide) and right column (narrow)

# Left column - Display the document and analysis output
with col1:
    uploaded_file = st.file_uploader("Upload a PDF, DOCX, or TXT file", type=["pdf", "docx", "txt"])

    if uploaded_file:
        file_type = uploaded_file.name.split(".")[-1]
        text = ""

        if file_type == "pdf":
            text = extract_text_from_pdf(uploaded_file)
        elif file_type == "docx":
            text = extract_text_from_docx(uploaded_file)
        elif file_type == "txt":
            text = extract_text_from_txt(uploaded_file)

        if text:
            st.subheader("📜 Extracted Document Text")
            st.text_area("Document Content", text, height=300)

            if st.button("🔍 Analyze with OpenAI"):
                with st.spinner("Analyzing with OpenAI..."):
                    ai_output = analyze_with_openai(text)

                st.subheader("🧠 AI Analysis Output")

                # Split output into sections
                sections = {
                    "Questions and Answers": "",
                    "Consequences of Signing": "",
                    "Subtopics": ""
                }

                for section in sections.keys():
                    match = re.search(rf"## {section}\n(.+?)(?=\n## |\Z)", ai_output, re.DOTALL)
                    if match:
                        sections[section] = match.group(1).strip()

                tab1, tab2, tab3 = st.tabs(["❓ Questions & Answers", "⚠️ Consequences", "📂 Subtopics"])

                with tab1:
                    st.markdown(sections["Questions and Answers"] or "No questions found.")

                with tab2:
                    st.markdown(sections["Consequences of Signing"] or "No consequences found.")

                with tab3:
                    st.markdown(sections["Subtopics"] or "No subtopics found.")
        else:
            st.warning("Could not extract any text from the uploaded file.")
    else:
        st.info("Please upload a document to begin.")

# Right column - Custom questions input
with col2:
    st.header("🧐 Ask a Question About the Document")
    user_question = st.text_input("Enter your question:")

    if user_question:
        with st.spinner("Getting answer..."):
            # Send the question to OpenAI
            prompt = f"Answer this question based on the document content:\n\n{
