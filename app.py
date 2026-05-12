import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("News Category Prediction App")

st.write("Enter News Article Below")

input_text = st.text_area("Enter News")

if st.button("Predict"):

    transformed_text = vectorizer.transform([input_text])

    prediction = model.predict(transformed_text)

    st.success(f"Predicted Category: {prediction[0]}")