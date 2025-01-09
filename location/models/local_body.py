# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin
from location.models.block import Block

from location.choices import LocalBodyTypeChoices


class LocalBody(TimestampedMetaModelMixin):

    name = models.CharField(max_length=200)
    local_body_type = models.CharField(
        max_length=12, choices=LocalBodyTypeChoices.choices
    )
    block = models.ForeignKey(
        Block, related_name="local_bodies", on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f"{self.name} | {self.block}"

    class Meta:
        verbose_name = "Local Body"
        verbose_name_plural = "Local Bodies"
        ordering = ["name"]
