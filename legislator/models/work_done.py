# -*- coding: utf-8 -*-

from django.db import models

from civic.models import Scheme
from common.models import TimestampedMetaModelMixin
from legislator.models.fund import Allocation
from location.models.sub_local_bodies import SubLocalBody


class WorkDone(TimestampedMetaModelMixin):

    fund = models.ForeignKey(
        Allocation,
        related_name="works_done",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    scheme = models.ForeignKey(
        Scheme,
        related_name="works_done",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    amount = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField()
    location = models.ForeignKey(
        SubLocalBody,
        related_name="works_done",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    year = models.PositiveIntegerField()

    def __str__(self):
        if self.fund:
            return f"{self.fund} | {self.amount} | {self.location} | {self.year}"
        else:
            return f"{self.scheme} | {self.location} | {self.year}"
