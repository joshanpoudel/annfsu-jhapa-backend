from django.db import models
from versatileimagefield.fields import VersatileImageField


class OurTeam(models.Model):
    president_name = models.CharField(max_length=100)
    president_image = VersatileImageField(upload_to="president/")

    vice_president_name = models.CharField(max_length=100)
    vice_president_image = VersatileImageField(upload_to="vice_president/")

    secretary_name = models.CharField(max_length=100)
    secretary_image = VersatileImageField(upload_to="secretary/")

    vice_secretary_name_1 = models.CharField(max_length=100, blank=True, null=True)
    vice_secretary_image_1 = VersatileImageField(
        upload_to="vice_secretary/", blank=True, null=True
    )

    vice_secretary_name_2 = models.CharField(max_length=100, blank=True, null=True)
    vice_secretary_image_2 = VersatileImageField(
        upload_to="vice_secretary/", blank=True, null=True
    )

    vice_secretary_name_3 = models.CharField(max_length=100, blank=True, null=True)
    vice_secretary_image_3 = VersatileImageField(
        upload_to="vice_secretary/", blank=True, null=True
    )

    treasurer_name = models.CharField(max_length=100)
    treasurer_image = VersatileImageField(
        upload_to="treasurer/", blank=True, null=True
    )

    def __str__(self):
        return "Our Team"

    class Meta:
        verbose_name = "Our Team"
        verbose_name_plural = "Our Team"
