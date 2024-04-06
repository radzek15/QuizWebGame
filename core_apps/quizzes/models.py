from django.db import models
from django.utils.translation import gettext_lazy as _lazy

from core_apps.questions.models import Question


class Quiz(models.Model):
    quiz_name = models.CharField(verbose_name=_lazy('Quiz Name'), unique=True, max_length=100)
    quiz_description = models.CharField(verbose_name='Short Quiz Description', max_length=250)
    questions = models.ManyToManyField(Question)

    class Meta:
        verbose_name = _lazy('Quiz')
        verbose_name_plural = _lazy('Quizzes')

    def __str__(self):
        return self.quiz_name
