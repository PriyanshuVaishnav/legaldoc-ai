import streamlit as st
from pdf_reader import extract_pdf_text
from ner_extractor import extract_entities
from summarizer import summarize_text
from report_generator import create_report

st.title("📄 LegalDoc AI - PDF Analyzer for Lawyers")

uploaded_file = st.file_uploader("Upload a legal PDF", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.info("Extracting text...")
    text = extract_pdf_text("temp.pdf")

    st.info("Summarizing document...")
    summary = summarize_text(text)

    st.info("Extracting entities...")
    entities = extract_entities(text)

    st.success("Summary and Entities extracted!")

    st.subheader("📌 Summary:")
    st.write(summary)

    st.subheader("📌 Key Entities:")
    st.write(entities)

    if st.button("Download Report"):
        create_report("Uploaded Case", summary, str(entities))
        with open("report.pdf", "rb") as f:
            st.download_button("Download Report PDF", f, file_name="legal_report.pdf")