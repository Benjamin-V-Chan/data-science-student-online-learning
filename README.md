# data-science-student-online-learning

# Project Overview

This project analyzes students' adaptability to online education based on various factors. It includes data preprocessing, exploratory data analysis, feature engineering, machine learning model training, and evaluation. The goal is to identify key factors influencing adaptability and predict students' adaptability levels.

# Folder Structure
```
project-root/
├── data/                 # Raw dataset
│   └── students_adaptability_level_online_education.csv
├── scripts/              # Scripts for data processing and modeling
│   ├── 01_preprocessing.py
│   ├── 02_eda.py
│   ├── 03_feature_engineering.py
│   ├── 04_model_training.py
│   ├── 05_evaluation.py
├── outputs/              # Results and trained models
│   ├── preprocessed_data.csv
│   ├── processed_data.csv
│   ├── adaptability_model.pkl
│   ├── eda_summary.csv
│   ├── model_evaluation.txt
│   ├── *.png (EDA plots)
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
```

# Usage

## 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file:
```sh
pip install -r requirements.txt
```

## 2. Run Data Preprocessing:
```sh
python scripts/01_preprocessing.py
```
This script loads and cleans the dataset, saving the preprocessed version to `outputs/preprocessed_data.csv`.

## 3. Run Exploratory Data Analysis:
```sh
python scripts/02_eda.py
```
This script generates statistical summaries and visualizations, saving outputs to `outputs/`.

## 4. Run Feature Engineering:
```sh
python scripts/03_feature_engineering.py
```
This script converts categorical variables into numerical form, saving the transformed dataset to `outputs/processed_data.csv`.

## 5. Train the Machine Learning Model:
```sh
python scripts/04_model_training.py
```
This script trains a classification model and saves it as `outputs/adaptability_model.pkl`.

## 6. Evaluate the Model:
```sh
python scripts/05_evaluation.py
```
This script evaluates the trained model, generating accuracy and classification reports saved in `outputs/model_evaluation.txt`.

# Requirements
- Python 3.x
- pandas
- matplotlib
- seaborn
- scikit-learn
- joblib

# Acknowledgments
**Dataset Name:** Students Adaptability Level in Online Education  
**Dataset Author:** Md. Mahmudul Hasan Suzan AND Nishat Ahmed Samrin  
**Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/mdmahmudulhasansuzan/students-adaptability-level-in-online-education)