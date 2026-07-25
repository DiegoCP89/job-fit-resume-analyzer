import pymupdf


def extract_text_from_pdf(resume):
    document = pymupdf.open(stream=resume.read(), filetype="pdf")

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text