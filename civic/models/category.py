# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin


class Category(TimestampedMetaModelMixin):

    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]
