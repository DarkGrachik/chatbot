from django.shortcuts import render
from .forms import ReviewForm
import os
# from .model import SentimentModel, RatingModel
from django.http import JsonResponse


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sentiment_model_directory = os.path.join(BASE_DIR, 'reviews', 'my_awesome_model', 'checkpoint-1563')
vectorizer_path = os.path.join(BASE_DIR, 'reviews', 'tfidf_vectorizer7.pkl')
model_path = os.path.join(BASE_DIR, 'reviews', 'movie_rating_model7.pkl')
# подключаю модели
# sentiment_model = SentimentModel(sentiment_model_directory)
# rating_model = RatingModel(model_path, vectorizer_path)
# вьюха
# def review_view(request):
#     sentiment = None
#     rating = None
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review_text = form.cleaned_data['review']
#             sentiment = sentiment_model.predict(review_text)
#             rating = rating_model.predict(review_text)  # рейтинг
#     else:
#         form = ReviewForm()

#     return render(request, 'home.html', {'form': form, 'sentiment': sentiment, 'rating': rating})

def chatbot_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')

        # Вы можете добавить логику для обработки сообщения, например:
        # sentiment = sentiment_model.predict(user_message)
        # rating = rating_model.predict(user_message)
        sentiment = 123
        rating = 345

        # Ответ от ИИ
        response = {
            'reply': f'Sentiment: {sentiment}, Rating: {rating}'  # Тут будет ответ вашего ИИ
        }
        return JsonResponse(response)

    return render(request, 'chatbot.html')  # Если запрос не POST, то отдать главную страницу