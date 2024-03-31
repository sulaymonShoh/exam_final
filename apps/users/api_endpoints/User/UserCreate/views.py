from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.api_endpoints.User.UserCreate.serializers import UserCreateSerializer
from apps.users.models import CustomUser


class UserCreateView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            existing_user = CustomUser.objects.filter(username=username).first()
            if existing_user:
                if existing_user.deleted:
                    existing_user.deleted = False
                    existing_user.save()
                else:
                    return Response(
                        {"error": "Username already exists"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            user = CustomUser.objects.create(username=username)
            user.set_password(password)
            user.save()
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


__all__ = ("UserCreateView",)
