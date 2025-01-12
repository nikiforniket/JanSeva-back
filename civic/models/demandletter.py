# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import get_user_model

from common.models import TimestampedMetaModelMixin


class DemandLetter(TimestampedMetaModelMixin):

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="demand_letters"
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
