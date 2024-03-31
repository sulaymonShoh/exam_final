from rest_framework.generics import DestroyAPIView

from apps.users.api_endpoints.User.UserDestroy.serializers import UserDestroySerializer
from apps.users.models import CustomUser


class UserDestroyView(DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDestroySerializer


__all__ = ("UserDestroyView",)
