# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin
from django.contrib.auth import get_user_model

from civic.choices import GeoLocationComplaintChoices

User = get_user_model()


class GeoLocationComplaint(TimestampedMetaModelMixin):

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="geolocation_complaints")
    complaint_type = models.CharField(choices=GeoLocationComplaintChoices.choices,
                                      max_length=20)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.id} | {self.user} -> {self.lat}, {self.long}"


class GeoLocationComplaintFiles(TimestampedMetaModelMixin):
    complaint = models.ForeignKey(GeoLocationComplaint, on_delete=models.CASCADE,
                                    related_name="files")
    file = models.FileField(upload_to="geolocation_complaints/")

    def __str__(self):
        return f"{self.id} -> {self.complaint}"
