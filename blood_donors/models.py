from django.db import models

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

LOCATION_CHOICES = (("Nepal", "Nepal"), ("Abroad", "Abroad"))


class BloodDonor(models.Model):
    full_name = models.CharField(max_length=255)
    blood_group = models.CharField(
        max_length=10, choices=BLOOD_GROUP_CHOICES, default="O+"
    )
    district = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    location = models.CharField(
        max_length=20, choices=LOCATION_CHOICES, default="Nepal"
    )
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.full_name}"
    
    class Meta:
        verbose_name = "Blood Donor"
        verbose_name_plural = "Blood Donors"
