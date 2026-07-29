from typing import cast

import pymupdf


def extract_text_from_pdf(resume):
    document = pymupdf.open(stream=resume.read(), filetype="pdf")

    text = ""

    for page in document:
        text += cast(str, page.get_text("text"))

    document.close()

    return text