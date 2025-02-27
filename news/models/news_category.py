# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin


class NewsCategory(TimestampedMetaModelMixin):

    name = models.CharField(max_length=150, unique=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} | {self.is_approved}"

    class Meta:
        verbose_name = "News Category"
        verbose_name_plural = "News Categories"
        ordering = ["name"]
