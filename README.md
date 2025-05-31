# Emotion Detector System For Machines Using Naive Bayes - Streamlit App

This project is a Streamlit-based web application for detecting emotions using machine learning models. The system incorporates two models trained to analyze emotions: **Logistic Regression** and **Naive Bayes**.

## Project Overview

- Two models were trained for emotion detection:
  - **Logistic Regression**
  - **Naive Bayes**

- Both models were initially trained on a small dataset, then further trained on a larger dataset to improve accuracy.

- After comparing performance, the best-performing model was incorporated into this Streamlit app to provide real-time emotion detection.

## Folder Structure

- `app.py` — Main Streamlit app code  
- `data/` — Folder containing datasets used for training  
- `models/` — Folder containing saved trained models  
- `Logistic Regression Model Training & Saving.ipynb` — Notebook for training and saving Logistic Regression model  
- `Naive Bayes Model Training & Saving.ipynb` — Notebook for training and saving Naive Bayes model  
- `requirements.txt` — Python dependencies for running the app  

## Usage

1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3.Run the Streamlit app:

   streamlit run app.py

Notes
The .ipynb_checkpoints folders are excluded from this repository.

API keys and private info are stored securely and excluded from this repository for security reasons.

Feel free to contribute or raise issues if you find any!

Author: Muhammad Hanzalah Habib
