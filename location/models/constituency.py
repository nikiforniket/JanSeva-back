# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin
from location.models.state import State
from common.choices import ElectionTypeChoices


class Constituency(TimestampedMetaModelMixin):

    name = models.CharField(max_length=200)
    no = models.PositiveIntegerField()
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name="constituencies"
    )
    election_type = models.CharField(max_length=10, choices=ElectionTypeChoices.choices)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="child_constituencies",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name} | {self.state}"

    class Meta:
        verbose_name = "Constituency"
        verbose_name_plural = "Constituencies"
        ordering = ["name", "state__name"]
