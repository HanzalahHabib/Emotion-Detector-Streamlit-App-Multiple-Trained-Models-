import streamlit as st
import pickle
import os
import pandas as pd

# Emotion label and emoji mappings
emotion_labels = {
    0: 'sadness',
    1: 'joy',
    2: 'love',
    3: 'anger',
    4: 'fear',
    5: 'surprise'
}
emoji_dict = {
    'sadness': '😢',
    'joy': '😊',
    'love': '❤️',
    'anger': '😠',
    'fear': '😨',
    'surprise': '😲'
}
# Load the model and vectorizer
with open("models/naive_bayes_model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)
# Set page config
st.set_page_config(page_title="Emotion Detector", layout="centered", page_icon="💬")
# UI styling
st.markdown("""
    <style>
    .stTextInput > div > div > input {
        font-size: 18px;
    }
    .emotion {
        font-size: 24px;
        font-weight: bold;
        color: #6c63ff;
    }
    .header {
        font-size: 36px;
        font-weight: 700;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)
# App Title
st.markdown('<div class="header">🎭 Emotion Detector</div>', unsafe_allow_html=True)
st.markdown("Enter any sentence or message below, and I’ll detect the underlying emotion!")
# Text input
user_input = st.text_input("🔍 Enter your text here:", placeholder="I am feeling amazing today!")
# Button
if st.button("Detect Emotion"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        vect_input = vectorizer.transform([user_input])
        prediction = model.predict(vect_input)[0]
        # Map prediction to emotion name
        emotion_name = emotion_labels.get(prediction, 'unknown')
        # Show emotion name
        st.markdown(f"**Predicted Emotion:**")
        st.markdown(f'<div class="emotion">{emotion_name.upper()}</div>', unsafe_allow_html=True)
        # Emoji dict (keep it outside ideally)
        emoji_dict = {
            'joy': '😊',
            'anger': '😡',
            'sadness': '😢',
            'fear': '😨',
            'love': '❤️',
            'surprise': '😲'
        }
        # Show emoji for predicted emotion
        emoji = emoji_dict.get(emotion_name.lower(), '❓')
        st.markdown(f"Emotion Emoji: {emoji}")




