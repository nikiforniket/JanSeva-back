# -*- coding: utf-8 -*-

import uuid

from django.db import models
from django.contrib.auth import get_user_model

from common.models import TimestampedMetaModelMixin

from civic.choices import DemandLetterStatusChoices


class DemandLetter(TimestampedMetaModelMixin):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="demand_letters"
    )
    status = models.CharField(
        choices=DemandLetterStatusChoices.choices,
        default=DemandLetterStatusChoices.REGISTERED,
        max_length=25,
    )
    subject = models.CharField(max_length=150)
    description = models.TextField()
    sign = models.FileField(upload_to="demand_letters/signs/", blank=True, null=True)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "Demand Letter"
        verbose_name_plural = "Demand Letters"
        ordering = ["-created_at"]
