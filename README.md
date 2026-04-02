# Symptom Diagnosis using MultinomialNB

A Simple machine learning project that predicts diseases based on the given patients symptoms.

# Abstract

This project implements a Symptom-Disease Prediction system using the Multinomial Naive Bayes algorithm. The model is trained on a Kaggle dataset containing 132 symptoms and 42 diseases, achieving 100% accuracy on the test data. Given a set of symptoms as input, the model predicts the most probable disease. The project includes a web-based interface built with Streamlit, allowing users to interactively select symptoms and receive instant disease predictions.

## Dataset
- Source: Kaggle - Disease Prediction Using Machine Learning
- 132 symptoms as features
- 42 diseases as target classes

## Model
- Algorithm: Multinomial Naive Bayes
- Accuracy: 100% on test data

## How to Run
1. Clone the repo
2. Install dependencies: `pip install pandas scikit-learn matplotlib seaborn jupyter`
3. Open `symptom_diagnosis.ipynb` in VS Code
4. Run all cells