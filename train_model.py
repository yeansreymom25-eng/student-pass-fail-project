import pandas as pd
import pickle
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("dataset/student-mat.csv")

# print(df.columns)
# print(df.head())

# exit()

# Create Pass/Fail target
df["result"] = df["G3"].apply(
    lambda grade: "Pass" if grade >= 10 else "Fail"
)

# Features
features = [
    "studytime",
    "failures",
    "absences",
    "health",
    "G1",
    "G2"
]

X = df[features]
y = df["result"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# MLflow
mlflow.set_experiment("Student Pass Fail Decision Tree")

with mlflow.start_run():

    model = DecisionTreeClassifier(
        max_depth=5,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("Accuracy:", accuracy)

    mlflow.log_param("model", "Decision Tree")
    mlflow.log_param("max_depth", 5)
    mlflow.log_metric("accuracy", accuracy)

    mlflow.sklearn.log_model(
        model,
        "decision_tree_model"
    )

    # Save model
    with open("model.pkl", "wb") as file:
        pickle.dump(model, file)

print("Model saved successfully!")
