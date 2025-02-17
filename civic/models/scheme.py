# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin

from civic.models.sector import Sector


class Scheme(TimestampedMetaModelMixin):

    name = models.CharField(max_length=255, unique=True)
    sector = models.ForeignKey(
        Sector,
        related_name="schemes",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    year = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} | {self.year} | {self.sector}"

    class Meta:
        verbose_name = "Scheme"
        verbose_name_plural = "Schemes"
        ordering = ["name"]
