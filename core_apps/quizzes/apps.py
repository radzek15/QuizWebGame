from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _lazy


class QuizzesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.quizzes'
    verbose_name = _lazy('Quizzes')
