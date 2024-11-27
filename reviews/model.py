import re
import math
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from joblib import load
from nltk.stem import WordNetLemmatizer
import nltk

from transformers import AutoModelForSequenceClassification, PreTrainedModel
import torch
import torch.nn as nn

# Заглушка для модели
class FakeModel(PreTrainedModel):
    def __init__(self, config):
        super().__init__(config)
        self.dummy_layer = nn.Linear(10, 2)  # Простой фиктивный слой

    def forward(self, input_ids, attention_mask=None):
        # Просто возвращаем случайные значения, как будто модель что-то предсказывает
        return torch.randn(input_ids.size(0), 2)  # Выход размером (batch_size, 2)

# Заменяем загрузку модели на использование заглушки
def get_model(model_directory=None):
    # Вместо загрузки модели с Hugging Face используем FakeModel
    # Обычно конфигурация модели должна быть получена, но для заглушки можно просто создать базовую конфигурацию
    from transformers import AutoConfig
    config = AutoConfig.from_pretrained("bert-base-uncased")  # Используем любую базовую конфигурацию
    return FakeModel(config)


# nltk.download('wordnet')
# nltk.download('stopwords')

# class SentimentModel:
#     def __init__(self, model_directory):
#         self.model_directory = model_directory
#         #self.model = AutoModelForSequenceClassification.from_pretrained(self.model_directory)
#         self.model = get_model(self.model_directory)
#         self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

#     def predict(self, text):
#         inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
#         with torch.no_grad():
#             outputs = self.model(**inputs)
#         logits = outputs.logits
#         predictions = torch.argmax(logits, dim=1)
#         predicted_label = "POSITIVE" if predictions.item() == 1 else "NEGATIVE"
#         return predicted_label


# class RatingModel:
#     def __init__(self, model_path, vectorizer_path):
#         self.model = load(model_path)  # модель
#         self.vectorizer = load(vectorizer_path)  # векторизатор
#         self.lemmatizer = WordNetLemmatizer()

#     def preprocess(self, text):
#         text = re.sub(r'\W', ' ', text)
#         text = text.lower()
#         words = text.split()
#         words = [self.lemmatizer.lemmatize(word) for word in words]
#         return ' '.join(words)

#     def predict(self, text):
#         processed_text = self.preprocess(text)  # Предобработка текста
#         vectorized_text = self.vectorizer.transform([processed_text])  # Векторизация
#         rating = self.model.predict(vectorized_text)[0]  # Итог
#         return rating