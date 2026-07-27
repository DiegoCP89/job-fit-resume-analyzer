from flask import Flask, render_template, request

from services.analyzer import analyze_resume
from services.pdf_extractor import extract_text_from_pdf
from services.text_processor import normalize_text

app = Flask(__name__)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() == "pdf"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    job_description = request.form["job_description"]

    # Validate uploaded data
    if "resume" not in request.files:
        return "No resume file uploaded."

    resume = request.files["resume"]

    if resume.filename == "":
        return "No resume file uploaded."

    if not allowed_file(resume.filename):
        return "Only PDF files are allowed."

    if not job_description.strip():
        return "Job description is required."

    resume_text = extract_text_from_pdf(resume)

    normalized_resume_text = normalize_text(resume_text)
    normalized_job_description = normalize_text(job_description)

    matched_words, missing_words, match_score = analyze_resume(
        normalized_resume_text,
        normalized_job_description,
    )

    if match_score >= 70:
        score_class = "high-score"
    elif match_score >= 40:
        score_class = "medium-score"
    else:
        score_class = "low-score"

    print("\nMatched words:")
    print(matched_words)

    print("\nMissing words:")
    print(missing_words)

    print("\nMatch score:")
    print(f"{match_score:.2f}%")

    print("\nResume filename:")
    print(resume.filename)

    print("\nResume content type:")
    print(resume.content_type)

    print("\nOriginal job description:")
    print(job_description)

    print("\nNormalized job description:")
    print(normalized_job_description)

    print("\nNormalized resume text:")
    print(normalized_resume_text)

    return render_template(
    "result.html",
    matched_words=sorted(matched_words),
    missing_words=sorted(missing_words),
    match_score=match_score,
    score_class=score_class,
)


if __name__ == "__main__":
    app.run(debug=True)