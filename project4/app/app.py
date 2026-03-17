import streamlit as st
import joblib

# Load saved model
model = joblib.load("../models/model.pkl")

# Load vectorizer
vectorizer = joblib.load("../models/vectorizer.pkl")

st.title("Email Spam Classifier")

st.write("Enter an email message to check if it is Spam or Not.")

# User input
email = st.text_area("Enter email text")

# Button
if st.button("Check Spam"):

    email_vector = vectorizer.transform([email])

    prediction = model.predict(email_vector)

    if prediction[0] == 1:
        st.error("This email is SPAM 🚨")
    else:
        st.success("This email is NOT Spam ✅")