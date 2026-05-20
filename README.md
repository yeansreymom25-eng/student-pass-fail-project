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
Dataset -> Decision Tree Model -> MLflow Tracking -> Flask API -> Streamlit UI -> Deployment

## Features Used
- studytime
- failures
- absences
- health
- G1
- G2

## Model Performance
Accuracy: 87.34%

## How to Run the Project Locally

### 1. Install requirements
```bash
pip install -r requirements.txt
```

### 2. Run Streamlit only
This is the easiest local option. The app loads `model.pkl` directly.

```bash
streamlit run app.py
```

### 3. Run Flask API + Streamlit UI
Use this mode when demonstrating the Flask API requirement.

Terminal 1:

```bash
python api.py
```

Terminal 2:

```bash
$env:API_URL="http://127.0.0.1:5001/predict"
streamlit run app.py
```

The Streamlit UI will send prediction requests to the Flask API when `API_URL` is set. If `API_URL` is not set, the app uses the trained model directly.

## Test the Flask API
With `python api.py` running, send a POST request:

```bash
curl -X POST http://127.0.0.1:5001/predict -H "Content-Type: application/json" -d "{\"studytime\":2,\"failures\":0,\"absences\":5,\"health\":3,\"G1\":10,\"G2\":10}"
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
