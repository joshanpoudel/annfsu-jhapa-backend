from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request

from authentication.models import User
from authentication.serializers import UserSerializer
from core.response import CustomResponse


class MembersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        users = User.objects.all()

        serializer = UserSerializer(instance=users, many=True)

        return CustomResponse.success(
            data=serializer.data, message="Members fetched successfully!"
        )
