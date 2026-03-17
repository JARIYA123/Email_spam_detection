# 📧 Email Spam Detection 

## 🚀 Project Overview

This project is a **Machine Learning-based Email Spam Classifier** that predicts whether a given email or message is **Spam** or **Not Spam (Ham)**.It uses **Natural Language Processing (NLP)** techniques and classification algorithms to analyze text data and make predictions.

---

## 🎯 Objectives

* Detect spam messages automatically
* Learn basic NLP techniques
* Understand ML classification workflow
* Build a deployable ML model

---

## 🧠 Machine Learning Workflow

```
Data Collection
      ↓
Text Preprocessing
      ↓
Feature Extraction (CountVectorizer)
      ↓
Model Training (Naive Bayes)
      ↓
Evaluation
      ↓
Prediction
```

---

## 📂 Project Structure

```
project4
│
├── data
│   └── spam.csv
│
├── notebooks
│   └── experiment.ipynb
│
├── models
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── src
│   └── train_model.py
│
├── app
│   └── app.py
│
└── README.md
```

---

## ⚙️ Technologies Used

* Python 🐍
* Scikit-learn
* Pandas
* Streamlit (for UI)
* Joblib (model saving)

---

## 🔍 Features

* Text preprocessing (lowercase, remove special characters)
* Stopword removal
* Text vectorization using CountVectorizer
* Model training using Multinomial Naive Bayes
* Model evaluation with accuracy score
* Real-time prediction using Streamlit

---

## 📊 Model Used

### Multinomial Naive Bayes

* Works well for text classification
* Fast and efficient
* Suitable for spam detection

---

## 📈 Accuracy

The model achieves approximately:

```
Accuracy: ~97%
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/JARIYA123/email-spam-detection.git
cd email-spam-detection
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Train the Model

```
cd src
python train_model.py
```

---

### 4️⃣ Run the Web App

```
cd ../app
streamlit run app.py
```

---

## 🧪 Example

**Input:**

```
Congratulations! You have won $1000 prize
```

**Output:**

```
Spam 🚨
```

---

## 💡 Future Improvements

* Use TF-IDF Vectorizer for better accuracy
* Try Logistic Regression / SVM
* Deploy using FastAPI
* Add Docker support
* Improve UI design

---

## 📚 Learning Outcomes

* Understanding NLP preprocessing
* Feature extraction techniques
* ML model training and evaluation
* Model deployment basics

---

## 🤝 Contributing

Feel free to fork this repository and contribute!

---

## ⭐ Acknowledgements

* Dataset: SMS Spam Collection Dataset
* Scikit-learn Documentation

---

## 📬 Contact

If you have any questions, feel free to reach out!

---
