# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin

from civic.models.category import Category


class Department(TimestampedMetaModelMixin):

    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category, related_name="departments", blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"
        ordering = ["name"]
