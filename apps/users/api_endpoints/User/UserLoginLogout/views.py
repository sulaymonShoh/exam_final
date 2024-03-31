from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.api_endpoints.User.UserLoginLogout.serializers import (
    UserLoginSerializer,
)


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                if user.deleted_at is not None:
                    raise PermissionDenied("User account is deleted")
                else:
                    login(request, user)
                    return Response(
                        {"message": "Login successful"}, status=status.HTTP_200_OK
                    )
            else:
                return Response(
                    {"error": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    authentication_classes = [IsAuthenticated, ]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response(
                    {"error": "Refresh token is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            from rest_framework_simplejwt.tokens import RefreshToken

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


__all__ = ("UserLoginView", "UserLogoutView")
