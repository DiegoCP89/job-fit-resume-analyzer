from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    job_description = request.form["job_description"]
    resume = request.files["resume"]

    print("Job description:")
    print(job_description)

    print("Resume filename:")
    print(resume.filename)

    print("Resume content type:")
    print(resume.content_type)

    return "Form received successfully."


if __name__ == "__main__":
    app.run(debug=True)