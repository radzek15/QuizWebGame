from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Question
from .pagination import QuestionPagination
from .serializers import QuestionSerializer


class QuestionListCreateView(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    pagination_class = QuestionPagination
    permission_classes = [IsAuthenticatedOrReadOnly]


class QuestionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]
