# -*- coding: utf-8 -*-

from django.contrib import admin
from civic.models import GeoLocationComplaint, GeoLocationComplaintFiles


class GeoLocationComplaintFilesInline(admin.TabularInline):
    model = GeoLocationComplaintFiles
    extra = 1  # Number of empty file fields to display by default
    fields = ("file", "created_at")
    readonly_fields = ("created_at",)
    verbose_name = "File"
    verbose_name_plural = "Files"


@admin.register(GeoLocationComplaint)
class GeoLocationComplaintAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "user",
        "complaint_type",
        "status",
        "lat",
        "long",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "complaint_type",
        "status",
        "created_at",
        "updated_at",
    )
    search_fields = ("uuid", "user__phone_number")
    ordering = ("-created_at",)
    readonly_fields = ("uuid", "created_at", "updated_at")
    fieldsets = (
        (
            "Complaint Information",
            {
                "fields": (
                    "uuid",
                    "user",
                    "complaint_type",
                    "status",
                    "lat",
                    "long",
                    "description",
                )
            },
        ),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
    inlines = [GeoLocationComplaintFilesInline]  # Add the inline here
