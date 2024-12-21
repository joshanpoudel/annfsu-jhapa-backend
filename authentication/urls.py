from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginView, ProfileView, RegisterView, UpdateProfilePictureView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("refresh-token/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", ProfileView.as_view(), name="auth_profile"),
    path(
        "profile-picture/",
        UpdateProfilePictureView.as_view(),
        name="auth_profile_picture",
    ),
]
