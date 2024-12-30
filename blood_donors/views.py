from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from django.db.models import Q

from core.notification import notify_user
from core.response import CustomResponse


from .serializers import BloodDonorSerializer, BloodRequestSerializer
from .models import BloodDonor
from authentication.models import User


class BloodDonorView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        full_name = request.query_params.get("full_name", None)
        address = request.query_params.get("address", None)
        blood_group = request.query_params.get("blood_group", None)
        location = request.query_params.get("location", None)

        donors = BloodDonor.objects.all().order_by("full_name")

        query = Q()
        if full_name:
            query &= Q(full_name__icontains=full_name)
        if address:
            query &= Q(address__icontains=address)
        if blood_group:
            blood_group = blood_group.replace("-pos", "+").replace("-neg", "-")
            query &= Q(blood_group__iexact=blood_group)
        if location:
            query &= Q(location__icontains=location)

        donors = donors.filter(query)

        serializer = BloodDonorSerializer(instance=donors, many=True)
        return CustomResponse.success(
            data=serializer.data, message="Blood donors fetched successfully!"
        )


class BloodRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serializer = BloodRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        users = User.objects.all()

        filtered_users = [user for user in users if user.id != request.user.id]

        full_name = serializer.data.get("full_name")
        phone = serializer.data.get("phone_number")
        blood_group = serializer.data.get("blood_group")
        address = serializer.data.get("address")

        for user in filtered_users:
            print(user)
            notify_user(
                user,
                "Blood Donation Request",
                f"Name: {full_name}\nPhone: {phone}\nBlood Group: {blood_group}\nAddress: {address}",
            )

        return CustomResponse.success(message="Blood request submitted successfully!")
