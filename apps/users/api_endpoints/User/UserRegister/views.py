from rest_authtoken.serializers import UserRegistrationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import CustomUser


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            existing_user = CustomUser.objects.filter(username=username).first()
            if existing_user:
                if existing_user.deleted_at is not None:
                    existing_user.restore()
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


__all__ = ("UserRegisterView",)
