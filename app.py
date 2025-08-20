import streamlit as st
import pickle
st.title("SMS Spam Classifier")
st.write("This app classifies SMS messages as spam or ham (not spam).")
id2label = {0: "ham", 1: "spam"}
import re
def preprocess_text(text):
    # Example preprocessing: lowercasing and removing punctuation
    text = text.replace('\n', ' ').strip()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    text = re.sub(r'\d+', '', text)  # Remove digits
    return text.lower()
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
message = st.text_input("Enter your SMS message:")
if st.button("Classify"):
    if message:
        message_counts = vectorizer.transform([message])
        prediction = model.predict(message_counts)
        label = id2label[prediction[0]]
        st.success(f"The message is classified as: **{label}**")
    else:
        st.error("Please enter a message to classify.")