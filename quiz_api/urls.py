from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/auth/', include('core_apps.users.urls')),
    path('api/question/', include('core_apps.questions.urls')),
    path('api/quiz/', include('core_apps.quizzes.urls')),
]
