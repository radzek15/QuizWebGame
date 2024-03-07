from django.db import models
from django.utils.translation import gettext_lazy as _lazy


class Question(models.Model):
    question_description = models.TextField(verbose_name=_lazy('Question description'), unique=True)
    correct_answer = models.CharField(verbose_name=_lazy('Correct_Answer'), max_length=50)
    wrong_answer1 = models.CharField(verbose_name=_lazy('Wrong Answer 1'), max_length=50)
    wrong_answer2 = models.CharField(verbose_name=_lazy('Wrong Answer 2'), max_length=50, blank=True)
    wrong_answer3 = models.CharField(verbose_name=_lazy('Wrong Answer 3'), max_length=50, blank=True)

    class Meta:
        verbose_name = _lazy('Question')
        verbose_name_plural = _lazy('Questions')

    def __str__(self):
        return f'Question {self.id}'
