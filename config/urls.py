from django.contrib import admin
from django.urls import path, include  # Добавляем include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),  # Связываем с urls.py приложения
]
