PHRASES = {
    "machine learning": "machine_learning",
    "artificial intelligence": "artificial_intelligence",
    "data science": "data_science",
}


def replace_phrases(text):
    for phrase, replacement in PHRASES.items():
        text = text.replace(phrase, replacement)

    return text
