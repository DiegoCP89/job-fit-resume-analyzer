from flask import Flask, render_template, request
from services.pdf_extractor import extract_text_from_pdf

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

    print("Resume filename:")
    print(resume.filename)

    print("Resume content type:")
    print(resume.content_type)

    print("Job description:")
    print(job_description)

    print()

    print("Resume text:")
    print(resume_text)

    return "Form received successfully."


if __name__ == "__main__":
    app.run(debug=True)