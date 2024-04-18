import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _lazy

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    id_key = models.BigAutoField(primary_key=True, editable=False, unique=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(verbose_name=_lazy('E-mail'), unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    join_date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        username = str(self.email).split('@')[0]
        return username

    class Meta:
        verbose_name = _lazy('user')
        verbose_name_plural = _lazy('users')
