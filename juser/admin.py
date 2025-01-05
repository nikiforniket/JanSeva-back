# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from juser.models import JanSevaUser
from juser.forms import JanSevaUserChangeForm, JanSevaUserCreationForm


@admin.register(JanSevaUser)
class JanSevaUserAdmin(UserAdmin):
    form = JanSevaUserChangeForm
    add_form = JanSevaUserCreationForm

    fieldsets = (
        ("User", {"fields": ("email", "username", "password")}),
        (
            "Other Information",
            {"fields": ("full_name", "phone_number", "last_login_at", "date_joined")},
        ),
        ("User Permissions", {"fields": ("is_superuser", "is_staff", "is_active")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "full_name",
                    "username",
                    "password",
                    "confirm_password",
                ),
            },
        ),
    )
    list_display = (
        "uuid",
        "email",
        "username",
        "is_active",
        "is_staff",
        "is_superuser",
        "last_login",
        "date_joined",
    )
    list_filter = ("is_active", "is_superuser", "is_staff")
    search_fields = ("email",)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin): ...
