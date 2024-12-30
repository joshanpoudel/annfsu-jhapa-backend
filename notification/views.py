from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from core.response import CustomResponse
from .models import Notification
from .serializers import FCMTokenSerializer, NotificationSerializer


class UpdateFCMTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serializer = FCMTokenSerializer(instance=request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse.success(message="FCM token updated successfully!")
        return CustomResponse.error(
            data=serializer.errors, message="Something went wrong!"
        )


class NotificationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        notifications = Notification.objects.all()

        serializer = NotificationSerializer(instance=notifications, many=True)

        return CustomResponse.success(
            data=serializer.data, message="Notifications fetched successfully!"
        )
