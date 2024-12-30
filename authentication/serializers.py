import typing as t

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import User
from versatileimagefield.serializers import VersatileImageFieldSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User) -> t.Dict[str, t.Any]:
        token = super().get_token(user)

        token["email"] = user.email
        token["type"] = user.type

        return token

    def validate(self, attrs: t.Dict[str, t.Any]) -> t.Dict[str, t.Any]:
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(username=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid email or password")

        if not user.is_active:
            raise serializers.ValidationError("User account is disabled")

        refresh = self.get_token(user)

        return {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs: dict) -> dict:
        email = attrs.get("email", "")
        password = attrs.get("password", "")

        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise serializers.ValidationError("Invalid email or password.")
            if not user.is_active:
                raise serializers.ValidationError("User account is disabled.")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")

        attrs["user"] = user
        return attrs


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "full_name",
            "gender",
            "blood_group",
            "contact_number",
            "address",
            "college_name",
            "position"
        )

    def create(self, validated_data: dict) -> User:
        validated_data["password"] = make_password(validated_data["password"])
        user = User.objects.create(**validated_data)
        return user


from rest_framework import serializers
from .models import User
from versatileimagefield.serializers import VersatileImageFieldSerializer

class UserSerializer(serializers.ModelSerializer):
    profile_picture = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "full_name",
            "gender",
            "blood_group",
            "contact_number",
            "address",
            "college_name",
            "position",
            "profile_picture",
        )



class UpdateProfilePictureSerializer(serializers.ModelSerializer):
    profile_picture = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )
    
    class Meta:
        model = User
        fields = ("profile_picture",)
