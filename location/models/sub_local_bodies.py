# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin
from location.models.local_body import LocalBody


class SubLocalBody(TimestampedMetaModelMixin):

    name = models.CharField(max_length=200)
    local_body = models.ForeignKey(
        LocalBody, related_name="sublocalbodies", on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Sub Local Body"
        verbose_name_plural = "Sub Local Bodies"
        ordering = ["name"]
