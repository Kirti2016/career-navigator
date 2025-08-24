import fitz  # PyMuPDF

def extract_text_from_pdf(data: bytes) -> str:
    text = ""
    pdf = fitz.open(stream=data, filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text
