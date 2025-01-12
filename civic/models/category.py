# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin
from civic.models.department import Department


class Category(TimestampedMetaModelMixin):

    name = models.CharField(max_length=255)
    department = models.ForeignKey(
        Department, related_name="categories", on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]
        unique_together = ["name", "department"]
