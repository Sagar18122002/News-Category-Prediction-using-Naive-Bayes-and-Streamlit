# News Category Prediction using Naive Bayes

## Project Overview
This project is a Machine Learning and NLP-based web application that predicts the category of a news article using the Multinomial Naive Bayes algorithm. The application is built using Streamlit and allows users to enter news text and get the predicted category instantly.

---

## Technologies Used
- Python
- Machine Learning
- Natural Language Processing (NLP)
- Scikit-learn
- Streamlit
- Pandas
- NumPy

---

## Algorithm Used
### Multinomial Naive Bayes
Multinomial Naive Bayes is mainly used for text classification problems. It works efficiently with word frequencies and TF-IDF features, making it suitable for news classification tasks.

---

## Dataset
The dataset contains:
- News text
- News category labels

### Categories
- Business
- Sports
- Politics
- Technology
- Entertainment

---

## Project Workflow

1. Data Collection
2. Text Preprocessing
3. TF-IDF Vectorization
4. Train-Test Split
5. Model Training using MultinomialNB
6. Model Evaluation
7. Streamlit Web Application Deployment

---

## Features
- Predicts news category from user input
- Interactive Streamlit interface
- NLP preprocessing using TF-IDF
- Fast and accurate predictions
- Simple and beginner-friendly project

---

## Folder Structure

```bash
News_NB_Project/
│
├── app.py
├── train.py
├── label_nb.csv
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
