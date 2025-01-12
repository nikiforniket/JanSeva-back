# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin


class State(TimestampedMetaModelMixin):

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"
        ordering = ["name"]
