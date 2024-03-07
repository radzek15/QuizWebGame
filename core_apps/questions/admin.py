from django.contrib import admin
from django.utils.translation import gettext_lazy as _lazy

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    ordering = ['id']
    list_display = ['id', 'question_description', 'correct_answer', 'wrong_answer1', 'wrong_answer2', 'wrong_answer3']
    list_display_links = ['id', 'question_description', 'correct_answer', 'wrong_answer1', 'wrong_answer2', 'wrong_answer3']

    fieldsets = [
        (_lazy('Basic'), {'fields': ['question_description', 'correct_answer', 'wrong_answer1']}),
        (_lazy('Additional'), {
            'classes': ['collapse'],
            'fields': ['wrong_answer2', 'wrong_answer3']
        }),
    ]


admin.site.register(Question, QuestionAdmin)
