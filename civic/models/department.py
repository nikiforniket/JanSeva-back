# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin


class Department(TimestampedMetaModelMixin):

    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"
        ordering = ["name"]
