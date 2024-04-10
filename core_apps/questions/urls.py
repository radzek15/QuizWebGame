from django.urls import path

from .views import QuestionListCreateView, QuestionRetrieveUpdateDestroyView

urlpatterns = [
    path('', QuestionListCreateView.as_view(), name='question-lc'),
    path('<int:id>/', QuestionRetrieveUpdateDestroyView.as_view(), name='question-rud'),
]
