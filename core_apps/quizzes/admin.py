from django.contrib import admin

from .models import Quiz


class QuizAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'quiz_name']
    list_display_links = ['id', 'quiz_name']


admin.site.register(Quiz, QuizAdmin)
