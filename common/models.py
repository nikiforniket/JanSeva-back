# -*- coding: utf-8 -*-

from django.db import models


class TimestampedMetaModelMixin(models.Model):

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def count(cls, **filters):
        if filters:
            return cls.objects.filter(**filters).count()
        return cls.objects.count()

    class Meta:
        abstract = True
