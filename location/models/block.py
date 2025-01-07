# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin
from location.models.constituency import Constituency


class Block(TimestampedMetaModelMixin):

    name = models.CharField(max_length=200)
    constituency = models.ForeignKey(
        Constituency, related_name="blocks", on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f"{self.name} | {self.constituency}"

    class Meta:
        verbose_name = "Block"
        verbose_name_plural = "Blocks"
        ordering = ["name"]
