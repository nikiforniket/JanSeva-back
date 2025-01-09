# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin
from civic.models.department import Department


class Category(TimestampedMetaModelMixin):

    name = models.CharField(max_length=100)
    department = models.ManyToManyField(
        Department, related_name="categories", blank=False
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]
