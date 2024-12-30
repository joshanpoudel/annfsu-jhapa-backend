from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from .serializers import FCMTokenSerializer

class UpdateFCMTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serializer = FCMTokenSerializer(instance=request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "FCM token updated successfully!"})
        return Response(serializer.errors, status=400)
