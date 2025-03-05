import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load processed dataset
df = pd.read_csv("../outputs/processed_data.csv")

# Split data into features and target
X = df.drop(columns=["adaptivity_level"])
y = df["adaptivity_level"]

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "../outputs/adaptability_model.pkl")
