# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import get_user_model

from common.models import TimestampedMetaModelMixin


class Demand(TimestampedMetaModelMixin):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="demands")
    description = models.TextField()

    def __str__(self):
        return f"{self.user}"