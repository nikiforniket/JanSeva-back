# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import get_user_model

from common.models import TimestampedMetaModelMixin
from location.models import Constituency
from legislator.choices import RepresentativeTypeChoices

User = get_user_model()


class Representative(TimestampedMetaModelMixin):

    user = models.OneToOneField(
        User, related_name="representative", on_delete=models.DO_NOTHING
    )
    representative_type = models.CharField(
        max_length=20, choices=RepresentativeTypeChoices.choices
    )
    address = models.TextField()
    constituency = models.ForeignKey(
        Constituency, related_name="representatives", on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f"{self.user} | {self.constituency}"

    class Meta:
        verbose_name = "Representative"
        verbose_name_plural = "Representatives"
