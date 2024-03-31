from django.core.exceptions import ValidationError
from rest_framework import serializers

from apps.users.models import CustomUser


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=32)
    password = serializers.CharField(max_length=32)
    password2 = serializers.CharField(max_length=32)

    class Meta:
        model = CustomUser
        fields = ["username", "password", "password1"]

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise ValidationError("Passwords must match!")
        return data
