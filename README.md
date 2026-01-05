# Resume Analyzer
A web application that analyzes resumes and compares them with job descriptions using NLP techniques (keyword matching).

## Overview
This project extracts text from resume PDFs and evaluates how well a resume
matches a given job description by identifying common skills and keywords.

## Features
- Resume PDF upload
- Job description analysis
- Skill matching using NLP
- Match percentage score

## Tech Stack
- Python
- Flask
- spaCy
- HTML/CSS

## How to Run
This project can be run locally by following these steps:
1. Clone the repository:
https://github.com/avaydas01/ai-resume-analyzer.git
2. Install required dependencies:
3. Run the Flask app:
4. Open your browser and go to `http://localhost:5000` to access the app.
> Note: The project has not been deployed online. It can be run locally for testing and demonstration purposes.
5. Upload a PDF resume and paste a job description to see the analysis.
> Note: This project has been tested in a local environment. A live deployment is not available.
---

## How It Works
1. Extracts text from uploaded PDF resumes using PyPDF2
2. Processes the job description and resume text
3. Compares skills and keywords to calculate a match score
4. Displays the match percentage and matched skills on a simple web interface

## Future Enhancements
- Improved skill extraction
- Resume recommendations
- Visualization dashboard
