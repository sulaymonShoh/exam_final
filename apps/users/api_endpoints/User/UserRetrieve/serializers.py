from rest_framework.serializers import ModelSerializer
from apps.users.models import CustomUser


class UserRetrieveSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email")
