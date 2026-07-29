from services.stop_words import remove_stop_words
from services.synonyms import replace_synonyms
from services.phrases import replace_phrases;

def analyze_resume(resume_text, job_description):
    """
    Compare the resume with the job description using keyword matching.

    Returns:
        tuple:
            matched_words: keywords found in both texts.
            missing_words: keywords required by the job but not found in the resume.
            match_score: compatibility percentage.
    """
    resume_text = replace_phrases(resume_text)
    job_description = replace_phrases(job_description)

    resume_words = set(resume_text.split())
    job_words = set(job_description.split())

    resume_words = replace_synonyms(resume_words)
    job_words = replace_synonyms(job_words)

    resume_words = remove_stop_words(resume_words)
    job_words = remove_stop_words(job_words)

    matched_words = job_words.intersection(resume_words)
    missing_words = job_words.difference(resume_words)

    match_score = len(matched_words) / len(job_words) * 100

    return matched_words, missing_words, match_score