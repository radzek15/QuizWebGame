from django.urls import path

from .views import QuestionListCreateView, QuestionRetrieveUpdateDestroyView

urlpatterns = [
    path('question/', QuestionListCreateView.as_view(), name='docker-lc'),
    path('question/<int:id>/', QuestionRetrieveUpdateDestroyView.as_view(), name='docker-rud'),
]
