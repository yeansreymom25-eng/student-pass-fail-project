# Student Pass/Fail Prediction using Decision Tree

## Project Description
This project predicts whether a student will Pass or Fail using a Decision Tree machine learning model.

The dataset used is Student Alcohol Consumption.

## Prediction Target
The target is created from the final grade G3:

- Pass: G3 >= 10
- Fail: G3 < 10

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Decision Tree
- MLflow
- Flask API for local API testing
- Streamlit UI
- GitHub
- Streamlit Community Cloud deployment

## Project Workflow
Dataset -> Decision Tree Model -> MLflow Tracking -> Trained model -> Streamlit UI -> Deployment

## Features Used
- studytime
- failures
- absences
- health
- G1
- G2

## Model Performance
Accuracy: 87.34%

## How to Run the Streamlit App Locally

### 1. Install requirements
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
streamlit run app.py
```

## Optional: Run the Flask API Locally
The Streamlit app predicts directly from `model.pkl` so it can deploy easily on Streamlit Community Cloud. The Flask API is still included for local API testing.

```bash
python api.py
```

## Deploy Without a Card
Use Streamlit Community Cloud:

1. Push this repository to GitHub.
2. Open https://share.streamlit.io/.
3. Sign in with GitHub.
4. Click "Create app".
5. Select this repository and branch `main`.
6. Set the main file path to `app.py`.
7. Click "Deploy".

No Render account or Visa card is required.
