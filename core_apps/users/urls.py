from dj_rest_auth.views import PasswordResetConfirmView
from django.urls import include, path

from .views import CustomUserDetailsView

urlpatterns = [
    path("", include('dj_rest_auth.urls')),
    path("user/", CustomUserDetailsView.as_view(), name='user_details'),
    path("registration/", include('dj_rest_auth.registration.urls')),
    path("password/reset/confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset",),
]
