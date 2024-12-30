from django.urls import path
from .views import NotificationView, UpdateFCMTokenView

urlpatterns = [
    path("update-fcm-token/", UpdateFCMTokenView.as_view(), name="update-fcm-token"),
    path("", NotificationView.as_view(), name="notification"),
]
