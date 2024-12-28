from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        "email",
        "full_name",
        "type",
        "gender",
        "blood_group",
        "contact_number",
        "address",
        "college_name",
        "position",
        "is_staff",
        "is_superuser",
        "date_joined",
    )
    search_fields = ("email", "full_name", "contact_number")
    list_filter = ("type", "gender", "blood_group", "is_staff", "is_superuser")
    ordering = ("-date_joined",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal Info"),
            {
                "fields": (
                    "full_name",
                    "gender",
                    "blood_group",
                    "contact_number",
                    "address",
                    "college_name",
                    "position",
                    "profile_picture",
                )
            },
        ),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser")}),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "full_name",
                    "gender",
                    "blood_group",
                    "contact_number",
                    "address",
                    "college_name",
                    "position",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    readonly_fields = ("date_joined", "last_login")

    def get_app_label(self):
        return '' 


# Register Admins
admin.site.register(User, CustomUserAdmin)
