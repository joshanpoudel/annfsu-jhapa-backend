from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request


from .serializers import BloodDonorSerializer
from .pagination import BloodDonorPagination
from .models import BloodDonor


class BloodDonorView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        donors = BloodDonor.objects.all().order_by("id")
        paginator = BloodDonorPagination()
        paginated_donors = paginator.paginate_queryset(donors, request)

        serializer = BloodDonorSerializer(instance=paginated_donors, many=True)

        return paginator.get_paginated_response(
            {"data": serializer.data, "message": "Blood donors fetched succesfully!"}
        )
