from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from django.db.models import Q


from .serializers import BloodDonorSerializer
from .pagination import BloodDonorPagination
from .models import BloodDonor


class BloodDonorView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        full_name = request.query_params.get("full_name", None)
        address = request.query_params.get("address", None)
        blood_group = request.query_params.get("blood_group", None)
        location = request.query_params.get("location", None)

        donors = BloodDonor.objects.all().order_by("id")

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

        paginator = BloodDonorPagination()
        paginated_donors = paginator.paginate_queryset(donors, request)

        serializer = BloodDonorSerializer(instance=paginated_donors, many=True)
        return paginator.get_paginated_response(
            {"data": serializer.data, "message": "Blood donors fetched successfully!"}
        )
