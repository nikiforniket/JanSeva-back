# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import get_user_model

from common.models import TimestampedMetaModelMixin

User = get_user_model()


class Suggestion(TimestampedMetaModelMixin):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="suggestions")
    description = models.TextField()

    def __str__(self):
        return f"{self.user}"
