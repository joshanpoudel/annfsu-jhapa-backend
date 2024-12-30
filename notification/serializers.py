from rest_framework import serializers
from authentication.models import User
from .models import Notification

class FCMTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["fcm_token"]

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ["title", "body"]