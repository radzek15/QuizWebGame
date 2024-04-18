from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True
        return representation


class CustomRegisterSerializer(RegisterSerializer):
    username = None
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        super().get_cleaned_data()
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }
