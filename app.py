# ======================================================
#Importing Necessary Libraries
# ======================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from resume_analyzer import analyze_resume

# ==================================================
# Page Config
# ==================================================

st.set_page_config(
page_title="AI Resume Screening System",
page_icon="🤖",
layout="wide")

# ==================================================
# Custom CSS
# ==================================================

st.markdown("""

<style>

.main {
    padding-top: 1rem;
}

.stMetric {
    background-color: #1e1e1e;
    padding: 15px;
    border-radius: 10px;
}

h1 {
    color: #4CAF50;
}

</style>

""", unsafe_allow_html=True)

# ==================================================
# Header
# ==================================================

st.markdown(
""" <h1 style='text-align:center;'>
🤖 AI Resume Screening System </h1>

<p style='text-align:center;'>
AI Powered Resume Analysis & Candidate Recommendation
</p>
""",
unsafe_allow_html=True)

st.divider()

# ==================================================
# Sidebar
# ==================================================

st.sidebar.header("📄 Upload Resume")

uploaded_file = st.sidebar.file_uploader(
"Choose PDF Resume",
type=["pdf"]
)

# ==================================================
# Main Analysis
# ==================================================

if not uploaded_file:
    st.info("📄 Upload a PDF Resume to begin analysis.")
    st.stop()

with st.spinner("Analyzing Resume..."):

    (
        match_percentage,
        skill_match_score,
        final_score,
        matched,
        missing,
        recommendation
    ) = analyze_resume(uploaded_file)

st.success("Resume Uploaded Successfully!")

# ==========================================
# Score Cards
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📄 TF-IDF Similarity",
        f"{match_percentage:.2f}%"
    )

with col2:
    st.metric(
        "🛠 Skill Match",
        f"{skill_match_score:.2f}%"
    )

with col3:
    st.metric(
        "🏆 Final Score",
        f"{final_score:.2f}%"
    )

st.divider()

# ==========================================
# Gauge Meter (Visualizing Final Score)
# ==========================================

st.subheader("📈 Resume Score Gauge")

gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=final_score,
    title={"text": "Resume Score"},
    gauge={
        "axis": {"range": [0, 100]},
        "bar": {"color": "green"},
        "steps": [
            {"range": [0, 40], "color": "#ff4b4b"},
            {"range": [40, 70], "color": "#ffa500"},
            {"range": [70, 100], "color": "#2e7c55"}
        ]
    }
))

st.plotly_chart(
    gauge,
    width="stretch"
)

st.divider()

# ==========================================
# Skills Section
# ==========================================

st.subheader("🛠 Skills Analysis")

col1, col2 = st.columns(2)

with col1:

    st.subheader("✅ Matched Skills")

    if matched:

        for skill in matched:
            st.success(skill)

    else:
        st.info("No matching skills found.")

with col2:

    st.subheader("❌ Missing Skills")

    if missing:

        for skill in missing:
            st.error(skill)

    else:
        st.success("No missing skills.")

st.divider()

# ==========================================
# Pie Chart
# ==========================================

st.subheader("📊 Skill Distribution")

chart_data = pd.DataFrame({
    "Category": ["Matched", "Missing"],
    "Count": [len(matched), len(missing)]
})

pie_chart = px.pie(
    chart_data,
    values="Count",
    names="Category",
    hole=0.5
)

st.plotly_chart(
    pie_chart,
    width="stretch"
)

st.divider()

# ==========================================
# Recommendation
# ==========================================

st.subheader("🎯 AI Recommendation")

if final_score >= 80:

    st.success(recommendation)

elif final_score >= 60:

    st.warning(recommendation)

else:

    st.error(recommendation)

st.divider()

# ==========================================
# Suggestions
# ==========================================

st.subheader("🚀 Improvement Suggestions")

if missing:

    for skill in missing:
        st.write(f"• Learn **{skill}**")

else:

    st.success(
        "No major skill gaps detected."
    )

st.divider()

# ==========================================
# Download Report
# ==========================================

report = f"""

AI Resume Screening Report

TF-IDF Similarity Score: {match_percentage:.2f}%

Skill Match Score: {skill_match_score:.2f}%

Final Score: {final_score:.2f}%

Recommendation:
{recommendation}

Matched Skills:
{', '.join(matched)}

Missing Skills:
{', '.join(missing)}
"""

st.download_button(
    label="📥 Download Report",
    data=report,
    file_name="resume_report.txt",
    mime="text/plain")
