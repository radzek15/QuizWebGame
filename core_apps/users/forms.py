from django.contrib.auth import forms, get_user_model
from django.forms import ValidationError

User = get_user_model()


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = ['email']

    error_messages = {'Email occupied': 'Email is already connected to existing account'}

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise ValidationError(self.error_messages['Email occupied'])


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User
