import streamlit as st
import requests

st.title("🎓 Student Pass/Fail Prediction")
st.write("Decision Tree model using Student Alcohol Consumption dataset")

studytime = st.slider("Study Time", 1, 4, 2)
failures = st.slider("Past Failures", 0, 4, 0)
absences = st.slider("Absences", 0, 100, 5)
health = st.slider("Health", 1, 5, 3)
G1 = st.slider("G1 Grade", 0, 20, 10)
G2 = st.slider("G2 Grade", 0, 20, 10)

if st.button("Predict"):
    data = {
        "studytime": studytime,
        "failures": failures,
        "absences": absences,
        "health": health,
        "G1": G1,
        "G2": G2
    }

    response = requests.post("http://127.0.0.1:5000/predict", json=data)
    prediction = response.json()["prediction"]

    if prediction == "Pass":
        st.success("Prediction: Pass ✅")
    else:
        st.error("Prediction: Fail ❌")