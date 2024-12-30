from rest_framework import serializers
from authentication.models import User

class FCMTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["fcm_token"]