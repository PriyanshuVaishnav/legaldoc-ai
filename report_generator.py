from fpdf import FPDF

def create_report(case_title, summary, entities, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, f"Case Title: {case_title}")
    pdf.ln()
    pdf.multi_cell(0, 10, f"Summary:\n{summary}")
    pdf.ln()
    pdf.multi_cell(0, 10, f"Entities:\n{entities}")
    pdf.output(filename)