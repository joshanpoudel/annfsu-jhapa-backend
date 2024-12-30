from rest_framework import serializers
from .models import BloodDonor


class BloodDonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodDonor
        fields = [
            "id",
            "full_name",
            "blood_group",
            "district",
            "address",
            "phone_number",
            "date_of_birth",
            "location",
            "email_address",
        ]

class BloodRequestSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    phone_number = serializers.CharField()
    blood_group = serializers.CharField()
    address = serializers.CharField()
