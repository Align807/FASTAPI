import fitz  # PyMuPDF

def extract_text_from_pdf(file: bytes) -> str:
    pdf_document = fitz.open(stream=file, filetype="pdf")
    text = ""
    for page in pdf_document:
        text += page.get_text()
    pdf_document.close()
    return text
