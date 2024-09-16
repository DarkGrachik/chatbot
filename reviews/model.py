import re
import math
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from joblib import load
from nltk.stem import WordNetLemmatizer
import nltk


nltk.download('wordnet')
nltk.download('stopwords')

class SentimentModel:
    def __init__(self, model_directory):
        self.model_directory = model_directory
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_directory)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_directory)

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits
        predictions = torch.argmax(logits, dim=1)
        predicted_label = "POSITIVE" if predictions.item() == 1 else "NEGATIVE"
        return predicted_label


class RatingModel:
    def __init__(self, model_path, vectorizer_path):
        self.model = load(model_path)  # модель
        self.vectorizer = load(vectorizer_path)  # векторизатор
        self.lemmatizer = WordNetLemmatizer()

    def preprocess(self, text):
        text = re.sub(r'\W', ' ', text)
        text = text.lower()
        words = text.split()
        words = [self.lemmatizer.lemmatize(word) for word in words]
        return ' '.join(words)

    def predict(self, text):
        processed_text = self.preprocess(text)  # Предобработка текста
        vectorized_text = self.vectorizer.transform([processed_text])  # Векторизация
        rating = self.model.predict(vectorized_text)[0]  # Итог
        return rating