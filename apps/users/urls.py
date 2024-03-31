from django.urls import path

from apps.users.api_endpoints.User import (
    UserListView,
    UserRegisterView,
    UserRetrieveView,
    UserUpdateView,
    UserCreateView,
    UserDestroyView,
    UserLoginView,
    UserLogoutView,
)

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("list/", UserListView.as_view(), name="user-list"),
    path("create/", UserCreateView.as_view(), name="user-create"),
    path("<pk>/", UserRetrieveView.as_view(), name="user-retrieve"),
    path("<pk>/update", UserUpdateView.as_view(), name="user-update"),
    path("<pk>/destroy", UserDestroyView.as_view(), name="user-destroy"),
]
