# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin
from legislator.models.representative import Representative


class Fund(TimestampedMetaModelMixin):

    amount = models.PositiveIntegerField(null=True, blank=True)
    year = models.PositiveIntegerField()
    description = models.TextField()
    representative = models.ForeignKey(Representative, related_name="funds", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.representative} | {self.amount} | {self.year}"

    class Meta:
        verbose_name = "Fund"
        verbose_name_plural = "Funds"
        unique_together = ["representative", "year"]
