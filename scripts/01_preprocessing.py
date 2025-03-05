import pandas as pd

# Load dataset
df = pd.read_csv("../data/students_adaptability_level_online_education.csv")

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Save preprocessed data
df.to_csv("../outputs/preprocessed_data.csv", index=False)
