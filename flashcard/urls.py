# flashcard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create-prompt/', views.create_prompt, name='create-prompt'),
    # Other URL patterns for your application
]
