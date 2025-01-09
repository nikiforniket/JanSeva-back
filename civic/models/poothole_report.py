# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin
from django.contrib.auth import get_user_model

User = get_user_model()


class PootholeReport(TimestampedMetaModelMixin):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poothole_reports")
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user}"