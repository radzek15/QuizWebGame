from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _lazy


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            raise ValueError(_lazy('Email is not valid.'))

    def create_user(self, email, password, **extra_fields):
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_lazy("Provide email address"))

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_lazy("Superuser must have is_staff=True."))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_lazy("Superuser must have is_superuser=True."))

        if not password:
            raise ValueError(_lazy("Superuser must have a password."))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_lazy('Provide email address'))

        user = self.create_user(email, password, **extra_fields)
        user.save(using=self._db)
        return user
