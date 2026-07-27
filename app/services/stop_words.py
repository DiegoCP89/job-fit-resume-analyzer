ENGLISH_STOP_WORDS = {
    "a",
    "an",
    "and",
    "at",
    "for",
    "in",
    "of",
    "on",
    "or",
    "the",
    "to",
    "with",
}


def remove_stop_words(words):
    """
    Remove common English stop words from a set of words.
    """
    return words.difference(ENGLISH_STOP_WORDS)