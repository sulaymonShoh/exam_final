from rest_framework.serializers import ModelSerializer

from apps.users.models import CustomUser


class UserDestroySerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", "email")
