from django.urls import path
from . import views

urlpatterns = [
    # path('', views.review_view, name='home'),  # Главная страница
    path('chatbot/', views.chatbot_view, name='chatbot'),  # Новый маршрут для чат-бота
]
