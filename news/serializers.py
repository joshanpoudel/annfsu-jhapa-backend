from rest_framework import serializers
from .models import News, Songs
from versatileimagefield.serializers import VersatileImageFieldSerializer


class NewsSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
            ("medium_square_crop", "crop__400x400"),
            ("small_square_crop", "crop__50x50"),
        ]
    )

    class Meta:
        model = News
        fields = ("id", "title", "body", "image", "created_at", "updated_at")
        read_only_fields = ("created_at", "updated_at")


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("id", "title", "youtube_url", "audio_file")
