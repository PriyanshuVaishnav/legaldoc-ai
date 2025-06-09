from pdfminer.high_level import extract_text

def extract_pdf_text(pdf_path):
    return extract_text(pdf_path)