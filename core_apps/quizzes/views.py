from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Quiz
from .serializers import QuizSerializer


class QuizListCreateView(generics.ListCreateAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class QuizRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]
