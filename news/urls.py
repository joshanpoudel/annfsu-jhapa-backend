from django.urls import path
from .views import NewsView, SongsView

urlpatterns = [
    path("news/", NewsView.as_view(), name="news"),
    path("songs/", SongsView.as_view(), name="songs"),
]
