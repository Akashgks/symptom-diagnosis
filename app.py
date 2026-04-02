import streamlit as st
import pandas as pd
from sklearn.naive_bayes import MultinomialNB

train = pd.read_csv("data/Training.csv")
test = pd.read_csv("data/Testing.csv")

train = train.drop(columns=['Unnamed: 133'], errors='ignore')

X_train = train.drop("prognosis", axis=1)
y_train = train["prognosis"]

model = MultinomialNB()
model.fit(X_train, y_train)

symptoms = X_train.columns.tolist()
display = [s.replace('_', ' ').title() for s in symptoms]

st.title("Symptom-Diagnosis using MultinomialNB")
st.write("Select your symptoms and click Predict to find out the disease.")

st.subheader("Select Symptoms:")
selected_display = st.multiselect("Choose your symptoms", display)
selected = [symptoms[display.index(s)] for s in selected_display]
if st.button("Predict"):
    if len(selected) == 0:
        st.warning("⚠️ Please select at least one symptom!")
    else:
        input = dict.fromkeys(symptoms, 0)
        for s in selected:
            input[s] = 1
        input_df = pd.DataFrame([input])
        pred1 = model.predict(input_df)
        st.success(f"Predicted Disease: **{pred1[0]}**")