# 🤖 AI-Powered Resume Screening System

An intelligent Resume Screening System built using Python, NLP, Machine Learning techniques, and Streamlit. This application analyzes resumes against job requirements, evaluates candidate suitability, and generates hiring recommendations through automated resume parsing and skill matching.

---

## 🚀 Features

* 📄 PDF Resume Upload
* 📝 Automated Resume Text Extraction
* 🔍 TF-IDF Based Resume Similarity Analysis
* 🛠 Skill Matching & Gap Identification
* 📊 Interactive Dashboard using Streamlit
* 📈 Resume Score Gauge Meter
* 🥧 Skill Distribution Visualization
* 🎯 AI-Based Candidate Recommendation
* 📥 Downloadable Resume Screening Report

---

## 🏗️ Tech Stack

### Programming Language

* Python

### Libraries & Frameworks

* Streamlit
* PDFPlumber
* Pandas
* NLTK
* Scikit-Learn
* Plotly

### NLP Techniques

* Tokenization
* Stopword Removal
* Lemmatization
* TF-IDF Vectorization
* Cosine Similarity

---

## 📂 Project Structure

```text
Resume_Screening_System/
|── __pycache__
|
├── screenshots/
│   ├── home_page.png
│   ├── upload_resume.png
│   ├── candidate_score.png
│   ├── skill_matching.png
│   |── ai_recommendation.png
|   └── improovements_&_download_report.png
│
|── .gitignore
├── app.py
├── jobs.txt
├── README.md
├── resume_analyzer.py

```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Resume_Screening_System.git
cd Resume_Screening_System
```
### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

The application will launch in your browser.

---

## 📊 Resume Evaluation Metrics

### TF-IDF Similarity Score

Measures textual similarity between the uploaded resume and job description.

### Skill Match Score

Evaluates how many required skills are present in the candidate's resume.

### Final Resume Score

Final Score = (70% Skill Match) + (30% TF-IDF Similarity)

---

## 🎯 Recommendation System

| Score Range | Recommendation         |
| ----------- | ---------------------- |
| 80% - 100%  | Selected for Interview |
| 60% - 79%   | Consider for Interview |
| Below 60%   | Not Recommended        |

---

## 📸 Screenshots

### 🏠 Home Page
![Home Page](./screenshots/1.home_page.png)

### 📤 Resume Upload Interface
![Resume Upload](./screenshots/2.upload_resume.png)

### 🎯 Candidate Score Analysis
![Candidate Score](./3.screenshots/candidate_score.png)

### 🔍 Skill Matching Overview
![Skill Matching](./4.screenshots/skill_matching.png)

### 📊 Ai Recommendation
![Ai Recommendation](./5.screenshots/ai_recommendation.png)

### 📊 Improovements
![Improovements](./6.screenshots/improovements_&_download_report.png)
---

## 🔮 Future Improvements

* Candidate Name Extraction
* Email & Phone Extraction
* Multiple Resume Ranking
* PDF Report Generation
* Job Description Upload
* Resume Database Integration
* AI-Based Resume Suggestions

---

## 👨‍💻 Author

**Chandan Bisht**

Aspiring AI/ML Engineer | Python Developer | Machine Learning Enthusiast

LinkedIn: Add Your LinkedIn Profile

GitHub: Add Your GitHub Profile

---

## ⭐ Support

If you found this project helpful, consider giving it a star on GitHub.
