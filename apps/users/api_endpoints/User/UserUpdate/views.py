from rest_framework.generics import UpdateAPIView

from apps.users.api_endpoints.User.UserUpdate.serializers import UserUpdateSerializer
from apps.users.models import CustomUser


class UserUpdateView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializer


__all__ = ("UserUpdateView",)
