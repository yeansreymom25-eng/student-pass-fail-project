from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return "Student Pass/Fail Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    input_data = pd.DataFrame([{
        "studytime": data["studytime"],
        "failures": data["failures"],
        "absences": data["absences"],
        "health": data["health"],
        "G1": data["G1"],
        "G2": data["G2"]
    }])

    prediction = model.predict(input_data)[0]

    return jsonify({
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)