from django.urls import path

from .views import QuizListCreateView, QuizRetrieveUpdateDestroyView

urlpatterns = [
    path('', QuizListCreateView.as_view(), name='quiz-lc'),
    path('<int:id>/', QuizRetrieveUpdateDestroyView.as_view(), name='quiz-rud'),
]
