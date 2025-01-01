from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from team.models import OurTeam


class TeamSerializer(serializers.ModelSerializer):
    president_image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
            ("medium_square_crop", "crop__400x400"),
            ("small_square_crop", "crop__50x50"),
        ]
    )
    vice_president_image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
            ("medium_square_crop", "crop__400x400"),
            ("small_square_crop", "crop__50x50"),
        ]
    )
    secretary_image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
            ("medium_square_crop", "crop__400x400"),
            ("small_square_crop", "crop__50x50"),
        ]
    )

    vice_secretary_image_1 = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
            ("medium_square_crop", "crop__400x400"),
            ("small_square_crop", "crop__50x50"),
        ]
    )

    vice_secretary_image_2 = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
            ("medium_square_crop", "crop__400x400"),
            ("small_square_crop", "crop__50x50"),
        ]
    )

    vice_secretary_image_3 = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
            ("medium_square_crop", "crop__400x400"),
            ("small_square_crop", "crop__50x50"),
        ]
    )

    treasurer_image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
            ("medium_square_crop", "crop__400x400"),
            ("small_square_crop", "crop__50x50"),
        ]
    )

    class Meta:
        model = OurTeam
        fields = [
            "president_name",
            "president_image",
            "vice_president_name",
            "vice_president_image",
            "secretary_name",
            "secretary_image",
            "vice_secretary_name_1",
            "vice_secretary_image_1",
            "vice_secretary_name_2",
            "vice_secretary_image_2",
            "vice_secretary_name_3",
            "vice_secretary_image_3",
            "treasurer_name",
            "treasurer_image",
        ]
