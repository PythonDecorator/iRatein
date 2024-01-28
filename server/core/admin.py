"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models  # noqa
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Permissions"), {"fields": ("is_active",
                                       "is_staff",
                                       "is_superuser")}),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    readonly_fields = ["last_login"]

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "first_name",
                "last_name",
                "email",
                "password1",
                "password2",
                "is_active",
                "is_staff",
                "is_ambassador",
            ),
        }),
    )


admin.site.register(models.User, UserAdmin)
