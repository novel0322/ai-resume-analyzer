import fitz  # PyMuPDF


def extract_pdf_text(file_bytes: bytes) -> str:
    text_list = []

    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        for page in doc:
            text = page.get_text("text", sort=True)
            text_list.append(text)

    return "\n".join(text_list)