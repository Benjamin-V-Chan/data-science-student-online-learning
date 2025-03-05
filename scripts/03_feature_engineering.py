import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load preprocessed dataset
df = pd.read_csv("../outputs/preprocessed_data.csv")

# Convert categorical variables to numerical
le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])

# Save transformed data
df.to_csv("../outputs/processed_data.csv", index=False)
