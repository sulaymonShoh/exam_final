from django.core.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from apps.users.models import CustomUser


class UserCreateSerializer(ModelSerializer):
    password1 = CharField(max_length=32)

    class Meta:
        model = CustomUser
        fields = ("username", "password", "password1")

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise ValidationError("Passwords must match!")
        return data
