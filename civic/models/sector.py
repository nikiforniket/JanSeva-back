# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin


class Sector(TimestampedMetaModelMixin):

    name = models.CharField(max_length=255, unique=True)


    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectors"
        ordering = ["name"]
