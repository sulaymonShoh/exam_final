from rest_framework.generics import ListAPIView

from apps.users.api_endpoints.User.UserList.serializers import UserListSerializer
from apps.users.models import CustomUser


class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer


__all__ = ("UserListView",)
