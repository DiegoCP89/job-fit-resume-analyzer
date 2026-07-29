SYNONYMS = {
    "js": "javascript",
    "py": "python",
    "ai": "artificial intelligence",
    "ml": "machine learning",
}


def replace_synonyms(words):
    normalized_words = set()

    for word in words:
        normalized_words.add(SYNONYMS.get(word, word))

    return normalized_words

