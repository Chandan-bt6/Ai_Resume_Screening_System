# ======================================================
# Importing Necessary Libraries
# ======================================================

import pdfplumber
import nltk
import re

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def analyze_resume(pdf_file):

# ======================================================
# Extract Resume Text
# ======================================================

    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

# ======================================================
# Load Job Description
# ======================================================

    with open("jobs.txt", "r", encoding="utf-8") as file:
        job = file.read().lower()

# =======================================================
# Resume Preprocessing
# ========================================================

    dataset = text.split("\n")

    dataset = [
        line.strip()
        for line in dataset
        if line.strip()
    ]

    for i in range(len(dataset)):
        dataset[i] = dataset[i].lower()
        dataset[i] = re.sub(r"\W", " ", dataset[i])
        dataset[i] = re.sub(r"\s+", " ", dataset[i])

# =====================================================
# Bag of Words
# ======================================================

    word2count = {}

    for data in dataset:

        words = nltk.word_tokenize(data)

        for word in words:

            if word not in word2count:
                word2count[word] = 1
            else:
                word2count[word] += 1

    stop_words = set(stopwords.words("english"))

    filtered_word2count = {
        word: count
        for word, count in word2count.items()
        if word not in stop_words
    }

# ======================================================
# TF-IDF Similarity
# =======================================================

    lemmatizer = WordNetLemmatizer()

    filtered_words = [
        lemmatizer.lemmatize(word)
        for word in filtered_word2count
    ]

    resume_text = " ".join(filtered_words)

    job = re.sub(r"\W", " ", job)
    job = re.sub(r"\s+", " ", job)

    documents = [resume_text, job]

    vectorizer = TfidfVectorizer()

    result = vectorizer.fit_transform(documents)

    score = cosine_similarity(
        result[0:1],
        result[1:2]
    )

    match_percentage = score[0][0] * 100

# ======================================================
# Skill Database
# ======================================================

    skill_database = [
        "python",
        "java",
        "c",
        "c++",
        "numpy",
        "Pandas",
        "matplotlib",
        "Seaborn",
        "scikit-learn",
        "tensorflow",
        "Pytorch",
        "machine learning",
        "deep learning",
        "nlp",
        "computer vision",
        "sql",
        "mysql",
        "postgresql",
        "flask",
        "django",
        "Fastapi",
        "git",
        "github",
        "linux",
        "docker",
        "kubernetes",
        "Aws",
        "azure",
        "gcp",
        "data analysis",
        "Statistics",
        "power bi",
        "tableau"
    ]

    matched = []
    missing = []

    for skill in skill_database:

        if skill in job:

            if skill in resume_text:
                matched.append(skill)
            else:
                missing.append(skill)

# ===============================================================
# Skill Match Score
# ================================================================

    total_required_skills = len(matched) + len(missing)

    if total_required_skills > 0:
        skill_match_score = (
            len(matched) / total_required_skills
        ) * 100
    else:
        skill_match_score = 0

# =============================================================
# Final Score
# =============================================================

    final_score = (
        0.7 * skill_match_score +
        0.3 * match_percentage
    )

# ===========================================================
# Recommendation
# ===========================================================

    if final_score >= 80:
        recommendation = "Selected for Interview"

    elif final_score >= 60:
        recommendation = "Consider for Interview"

    else:
        recommendation = "Not Recommended"

    # ==============================
    # Return Results
    # ==============================

    return (
        match_percentage,
        skill_match_score,
        final_score,
        matched,
        missing,
        recommendation
    )