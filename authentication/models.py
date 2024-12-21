from django.contrib.auth.models import AbstractUser
from django.db import models

USER_TYPE_CHOICES = (("admin", "Administrator"), ("user", "User"))
GENDER_CHOICES = (("male", "Male"), ("female", "Female"), ("other", "Other"))

BLOOD_GROUP_CHOICES = (
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("O+", "O+"),
    ("O-", "O-"),
)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default="user")
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    contact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)

    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class BlacklistedToken(models.Model):
    token = models.CharField(max_length=255, unique=True)
