import random
import string
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from versatileimagefield.fields import VersatileImageField

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


def generate_unique_username():
    """Generate a random unique username"""
    random_string = "".join(random.choices(string.ascii_letters + string.digits, k=6))
    return f"{random_string}"


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular user with an email and password."""
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser with an email, password, and admin privileges."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        user = self.create_user(email, password, **extra_fields)
        user.username = generate_unique_username()
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default="user")
    full_name = models.CharField(max_length=255, default="Unknown")
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="male")
    blood_group = models.CharField(
        max_length=3, choices=BLOOD_GROUP_CHOICES, default="O+"
    )
    contact_number = models.CharField(max_length=15, default="9800000000")
    address = models.CharField(max_length=100, default="Unknown")
    college_name = models.CharField(max_length=100, default="Unknown")
    position = models.CharField(max_length=50, default="Unknown")

    profile_picture = VersatileImageField(
        upload_to='profile_pictures/',
        width_field='width',
        height_field='height'
    )

    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)

    fcm_token = models.TextField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class BlacklistedToken(models.Model):
    token = models.CharField(max_length=255, unique=True)
