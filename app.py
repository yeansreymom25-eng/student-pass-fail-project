import streamlit as st
import requests

st.set_page_config(
    page_title="Student Pass/Fail Prediction",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #f7f9fc;
}
.title-box {
    background: linear-gradient(135deg, #1f4e79, #4f8fcf);
    padding: 35px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}
.card {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}
.metric-card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.08);
}
.pass-box {
    background-color: #d9f7e5;
    color: #137333;
    padding: 25px;
    border-radius: 18px;
    font-size: 26px;
    font-weight: bold;
    text-align: center;
}
.fail-box {
    background-color: #fde2e2;
    color: #b3261e;
    padding: 25px;
    border-radius: 18px;
    font-size: 26px;
    font-weight: bold;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-box">
    <h1>🎓 Student Pass/Fail Prediction</h1>
    <p>Decision Tree Machine Learning System</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="metric-card"><h3>Model</h3><p>Decision Tree</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card"><h3>Accuracy</h3><p>87.34%</p></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card"><h3>Prediction</h3><p>Pass / Fail</p></div>', unsafe_allow_html=True)

st.write("")

left, right = st.columns([1.2, 1])

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📋 Enter Student Information")

    studytime = st.slider("Study Time", 1, 4, 2)
    failures = st.slider("Past Failures", 0, 4, 0)
    absences = st.slider("Absences", 0, 100, 5)
    health = st.slider("Health", 1, 5, 3)
    G1 = st.slider("G1 Grade", 0, 20, 10)
    G2 = st.slider("G2 Grade", 0, 20, 10)

    predict_button = st.button("🔍 Predict Result", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📌 Project Information")

    st.write("""
    This application predicts whether a student will **Pass** or **Fail**
    using a Decision Tree Machine Learning model.
    """)

    st.write("### Features Used")
    st.write("- Study time")
    st.write("- Past failures")
    st.write("- Absences")
    st.write("- Health")
    st.write("- G1 grade")
    st.write("- G2 grade")

    st.write("### Tools")
    st.write("Python, Flask, Streamlit, MLflow, GitHub")

    st.markdown('</div>', unsafe_allow_html=True)

st.write("")

if predict_button:
    data = {
        "studytime": studytime,
        "failures": failures,
        "absences": absences,
        "health": health,
        "G1": G1,
        "G2": G2
    }

    try:
        response = requests.post("http://127.0.0.1:5000/predict", json=data)
        prediction = response.json()["prediction"]

        if prediction == "Pass":
            st.markdown('<div class="pass-box">✅ Prediction: PASS</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="fail-box">❌ Prediction: FAIL</div>', unsafe_allow_html=True)

    except:
        st.error("Flask API is not running. Please run: python api.py")

st.write("")
st.markdown("---")
st.caption("Group 3 — Decision Tree | Student Alcohol Consumption Dataset")