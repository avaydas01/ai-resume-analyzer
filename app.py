"""
AI Resume Analyzer
Description: Analyze resume and job description using NLP
"""

from flask import Flask, render_template, request
import PyPDF2
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

def calculate_match(resume_text, jd_text):
    resume_words = set(resume_text.split())
    jd_words = set(jd_text.split())
    matched = resume_words.intersection(jd_words)
    score = (len(matched) / len(jd_words)) * 100
    return round(score, 2), list(matched)

@app.route("/", methods=["GET", "POST"])
def home():
    score = None
    skills = []

    if request.method == "POST":
        resume = request.files["resume"]
        jd = request.form["jd"]
        resume_text = extract_text(resume)
        score, skills = calculate_match(resume_text, jd.lower())

    return render_template("index.html", score=score, skills=skills)

if __name__ == "__main__":
    app.run(debug=True)
