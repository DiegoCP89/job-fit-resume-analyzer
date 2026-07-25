import string


def normalize_text(text):
    """
    Normalize text before comparing the resume
    with the job description.
    """
    normalized_text = text.lower()
    normalized_text = normalized_text.replace("\n", " ")
    normalized_text = normalized_text.translate(
        str.maketrans("", "", string.punctuation)
    )
    normalized_text = " ".join(normalized_text.split())

    return normalized_text