from rest_framework.generics import RetrieveAPIView, get_object_or_404

from apps.users.api_endpoints.User.UserRetrieve.serializers import (
    UserRetrieveSerializer,
)
from apps.users.models import CustomUser


class UserRetrieveView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRetrieveSerializer

    def get_object(self):
        user = get_object_or_404(CustomUser, pk=self.kwargs["pk"])
        return user


__all__ = ("UserRetrieveView",)
