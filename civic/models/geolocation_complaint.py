# -*- coding: utf-8 -*-
import uuid

from django.db import models

from common.models import TimestampedMetaModelMixin
from django.contrib.auth import get_user_model

from civic.choices import GeoLocationComplaintChoices, ComplaintStatusChoices

User = get_user_model()


class GeoLocationComplaint(TimestampedMetaModelMixin):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="geolocation_complaints"
    )
    complaint_type = models.CharField(
        choices=GeoLocationComplaintChoices.choices, max_length=20
    )
    status = models.CharField(
        choices=ComplaintStatusChoices.choices,
        default=ComplaintStatusChoices.REGISTERED,
        max_length=25,
    )
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.uuid} | {self.user} | {self.lat}, {self.long}"


class GeoLocationComplaintFiles(TimestampedMetaModelMixin):
    complaint = models.ForeignKey(
        GeoLocationComplaint,
        on_delete=models.CASCADE,
        related_name="files",
        to_field="uuid",
    )
    file = models.FileField(upload_to="geolocation_complaints/")

    def __str__(self):
        return f"{self.id} -> {self.complaint}"
