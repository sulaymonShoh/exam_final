from rest_framework.serializers import ModelSerializer

from apps.users.models import CustomUser


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
        )
