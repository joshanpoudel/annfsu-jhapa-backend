from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from core.response import CustomResponse

from .serializers import NewsSerializer, SongsSerializer

from .models import News, Songs

class NewsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        news = News.objects.all()

        serializer = NewsSerializer(instance=news, many=True)

        return CustomResponse.success(
            data=serializer.data,
            message="News fetched successfully!"
        )

class SongsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        songs = Songs.objects.all()

        serializer = SongsSerializer(instance=songs, many=True)

        return CustomResponse.success(
            data=serializer.data,
            message="Songs fetched successfully!"
        )


