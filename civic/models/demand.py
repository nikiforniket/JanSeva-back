# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import get_user_model

from common.models import TimestampedMetaModelMixin


class Demand(TimestampedMetaModelMixin):

    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name="demands")
    subject = models.CharField(max_length=150)
    description = models.TextField()
    sign = models.FileField(upload_to="demands/signs/", blank=True, null=True)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "Demand"
        verbose_name_plural = "Demands"
        ordering = ["-created_at"]