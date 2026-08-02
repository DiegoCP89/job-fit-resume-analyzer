def generate_feedback(match_score):
    if match_score >= 90:
        return (
            "Excellent compatibility!",
            "Your resume is highly aligned with this job."
        )

    elif match_score >= 70:
        return (
            "Good compatibility.",
            "Your resume matches most of the job requirements."
        )

    elif match_score >= 50:
        return (
            "Moderate compatibility.",
            "Consider improving the missing skills."
        )

    else:
        return (
            "Low compatibility.",
            "Consider improving your resume based on the job requirements."
        )


def get_score_class(match_score):
    if match_score >= 70:
        return "high-score"
    elif match_score >= 40:
        return "medium-score"
    else:
        return "low-score"
    

def generate_recommendations(missing_skills):
    """
    Generate a list of recommended skills based on the missing skills.
    """

    return sorted(missing_skills)