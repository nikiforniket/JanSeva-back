# -*- coding: utf-8 -*-

import uuid

from django.db import models
from django.contrib.auth import get_user_model

from common.models import TimestampedMetaModelMixin
from civic.models.sector import Sector
from civic.models.category import Category
from civic.choices import ComplaintStatusChoices

from location.models import SubLocalBody

User = get_user_model()


class Complaint(TimestampedMetaModelMixin):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="complaints")
    department = models.ForeignKey(
        Sector, on_delete=models.DO_NOTHING, related_name="complaints"
    )
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, related_name="complaints"
    )
    content = models.TextField()
    status = models.CharField(
        choices=ComplaintStatusChoices.choices,
        default=ComplaintStatusChoices.REGISTERED,
        max_length=25,
    )
    location = models.ForeignKey(
        SubLocalBody, related_name="complaints", on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f"{self.user} | {self.department} | {self.category}"

    class Meta:
        verbose_name = "Complaint"
        verbose_name_plural = "Complaints"
        ordering = ["-created_at"]
