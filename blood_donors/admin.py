from django.contrib import admin
from .models import BloodDonor

class BloodDonorAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "blood_group",
        "district",
        "address",
        "phone_number",
        "date_of_birth",
        "location",
        "email_address",
    )
    search_fields = ("full_name", "blood_group", "district", "phone_number", "email_address")
    list_filter = ("blood_group", "location", "district")
    ordering = ("full_name",)
    fields = (
        "full_name",
        "blood_group",
        "date_of_birth",
        "phone_number",
        "email_address",
        "address",
        "district",
        "location",
    )

admin.site.register(BloodDonor, BloodDonorAdmin)
