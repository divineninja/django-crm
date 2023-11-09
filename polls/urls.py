# polls/urls.py
from django.urls import path
from .views import QuestionList

urlpatterns = [
    path('api/questions/', QuestionList.as_view(), name='question-list'),
]
