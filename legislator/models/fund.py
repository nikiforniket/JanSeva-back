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


class Allocation(TimestampedMetaModelMixin):

    amount = models.PositiveIntegerField()
    fund = models.ForeignKey(Fund, related_name="allocations", on_delete=models.DO_NOTHING)
    month_start = models.PositiveIntegerField()
    month_end = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.fund} | {self.amount}"

    class Meta:
        verbose_name = "Allocation"
        verbose_name_plural = "Allocations"
