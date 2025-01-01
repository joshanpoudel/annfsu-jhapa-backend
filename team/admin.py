from django.contrib import admin
from django.utils.html import mark_safe
from .models import OurTeam


@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ("__str__",)

    def has_add_permission(self, request):
        if OurTeam.objects.exists():
            return False
        return super().has_add_permission(request)

    def save_model(self, request, obj, form, change):
        if not change and OurTeam.objects.exists():
            raise ValueError("You can only have one OurTeam instance.")
        super().save_model(request, obj, form, change)

    def president_image_preview(self, obj):
        if obj.president_image:
            return mark_safe(
                f'<img src="{obj.president_image.url}" style="max-width: 200px; margin-top: 10px;" />'
            )
        return "No image"

    def vice_president_image_preview(self, obj):
        if obj.vice_president_image:
            return mark_safe(
                f'<img src="{obj.vice_president_image.url}" style="max-width: 200px; margin-top: 10px;" />'
            )
        return "No image"

    def secretary_image_preview(self, obj):
        if obj.secretary_image:
            return mark_safe(
                f'<img src="{obj.secretary_image.url}" style="max-width: 200px; margin-top: 10px;" />'
            )
        return "No image"

    def vice_secretary_image_1_preview(self, obj):
        if obj.vice_secretary_image_1:
            return mark_safe(
                f'<img src="{obj.vice_secretary_image_1.url}" style="max-width: 200px; margin-top: 10px;" />'
            )
        return "No image"

    def vice_secretary_image_2_preview(self, obj):
        if obj.vice_secretary_image_2:
            return mark_safe(
                f'<img src="{obj.vice_secretary_image_2.url}" style="max-width: 200px; margin-top: 10px;" />'
            )
        return "No image"

    def vice_secretary_image_3_preview(self, obj):
        if obj.vice_secretary_image_3:
            return mark_safe(
                f'<img src="{obj.vice_secretary_image_3.url}" style="max-width: 200px; margin-top: 10px;" />'
            )
        return "No image"

    def treasurer_image_preview(self, obj):
        if obj.treasurer_image:
            return mark_safe(
                f'<img src="{obj.treasurer_image.url}" style="max-width: 200px; margin-top: 10px;" />'
            )

        return "No image"

    fieldsets = (
        (
            "President",
            {
                "fields": (
                    "president_name",
                    "president_image",
                    "president_image_preview",
                ),
                "description": "Details for the President.",
            },
        ),
        (
            "Vice President",
            {
                "fields": (
                    "vice_president_name",
                    "vice_president_image",
                    "vice_president_image_preview",
                ),
                "description": "Details for the Vice President.",
            },
        ),
        (
            "Secretary",
            {
                "fields": (
                    "secretary_name",
                    "secretary_image",
                    "secretary_image_preview",
                ),
                "description": "Details for the Secretary (optional).",
            },
        ),
        (
            "Vice Secretaries",
            {
                "fields": (
                    "vice_secretary_name_1",
                    "vice_secretary_image_1",
                    "vice_secretary_image_1_preview",
                    "vice_secretary_name_2",
                    "vice_secretary_image_2",
                    "vice_secretary_image_2_preview",
                    "vice_secretary_name_3",
                    "vice_secretary_image_3",
                    "vice_secretary_image_3_preview",
                ),
                "description": "Details for the Vice Secretaries (optional).",
            },
        ),
        (
            "Treasurer",
            {
                "fields": (
                    "treasurer_name",
                    "treasurer_image",
                    "treasurer_image_preview",
                ),
                "description": "Details for the Treasurer.",
            },
        ),
    )

    readonly_fields = (
        "president_image_preview",
        "vice_president_image_preview",
        "secretary_image_preview",
        "vice_secretary_image_1_preview",
        "vice_secretary_image_2_preview",
        "vice_secretary_image_3_preview",
        "treasurer_image_preview",
    )
