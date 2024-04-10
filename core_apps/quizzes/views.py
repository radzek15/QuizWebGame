from rest_framework import generics

from .models import Quiz
from .serializers import QuizSerializer


class QuizListCreateView(generics.ListCreateAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class QuizRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    lookup_field = 'id'
