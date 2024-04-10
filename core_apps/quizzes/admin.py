from django.contrib import admin

from .models import Quiz


class QuizAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'quiz_name', 'quiz_description']
    list_display_links = ['id', 'quiz_name', 'quiz_description']
    filter_horizontal = ['questions']


admin.site.register(Quiz, QuizAdmin)
