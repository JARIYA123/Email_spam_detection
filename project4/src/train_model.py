import pandas as pd
import re
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


# -------------------------
# 1 Load Dataset
# -------------------------

df = pd.read_csv("../data/spam.csv", encoding="latin-1")

df = df[['class','message']]


# -------------------------
# 2 Convert Labels
# -------------------------

df['class'] = df['class'].map({'ham':0,'spam':1})


# -------------------------
# 3 Text Cleaning Function
# -------------------------

def clean_text(text):

    text = text.lower()

    text = re.sub('[^a-zA-Z]', ' ', text)

    return text


df['message'] = df['message'].apply(clean_text)


# -------------------------
# 4 Text Vectorization
# -------------------------

vectorizer = CountVectorizer(stop_words='english')

X = vectorizer.fit_transform(df['message'])

y = df['class']


# -------------------------
# 5 Train Test Split
# -------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)


# -------------------------
# 6 Train Model
# -------------------------

model = MultinomialNB()

model.fit(X_train,y_train)


# -------------------------
# 7 Evaluate Model
# -------------------------

y_pred = model.predict(X_test)

print("Accuracy:",accuracy_score(y_test,y_pred))


# -------------------------


# 8 Save Model
# -------------------------

os.makedirs("../models",exist_ok=True)

joblib.dump(model,"../models/model.pkl")

joblib.dump(vectorizer,"../models/vectorizer.pkl")

print("Model saved successfully!")