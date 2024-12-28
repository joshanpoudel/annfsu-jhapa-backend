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
