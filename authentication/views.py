from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    LoginSerializer,
    RegisterSerializer,
    CustomTokenObtainPairSerializer,
    UpdateProfilePictureSerializer,
    UserSerializer,
)
from rest_framework.request import Request
from typing import Any
from core.response import CustomResponse


class LoginView(APIView):
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        refresh = CustomTokenObtainPairSerializer.get_token(user)

        return CustomResponse.success(
            data={
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            },
            message="User logged in successfully!",
        )


class RegisterView(APIView):
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = CustomTokenObtainPairSerializer.get_token(user)

        return CustomResponse.success(
            data={
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            },
            message="User registered successfully!",
        )


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        user = request.user

        del user.password

        serializer = UserSerializer(instance=user)

        return CustomResponse.success(
            data=serializer.data, message="Profile fetched successfully!"
        )


class UpdateProfilePictureView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        user = request.user
        serializer = UpdateProfilePictureSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return CustomResponse.success(
            data={"profile_picture": serializer.data["profile_picture"]},
            message="Profile picture updated successfully!",
        )
