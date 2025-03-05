import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed dataset
df = pd.read_csv("../outputs/preprocessed_data.csv")

# Generate summary statistics
summary = df.describe(include='all')
summary.to_csv("../outputs/eda_summary.csv")

# Visualize categorical variable distributions
for col in df.columns:
    plt.figure(figsize=(8, 4))
    sns.countplot(y=df[col], order=df[col].value_counts().index)
    plt.title(f"Distribution of {col}")
    plt.savefig(f"../outputs/{col}_distribution.png")
    plt.close()
