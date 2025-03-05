import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load processed dataset
df = pd.read_csv("../outputs/processed_data.csv")
X = df.drop(columns=["adaptivity_level"])
y = df["adaptivity_level"]

# Load trained model
model = joblib.load("../outputs/adaptability_model.pkl")

# Make predictions
y_pred = model.predict(X)

# Evaluate model performance
accuracy = accuracy_score(y, y_pred)
report = classification_report(y, y_pred)

# Save evaluation results
with open("../outputs/model_evaluation.txt", "w") as f:
    f.write(f"Accuracy: {accuracy:.4f}\n\n")
    f.write(report)
