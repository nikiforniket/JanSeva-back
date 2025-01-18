# -*- coding: utf-8 -*-

import uuid

from django.db import models
from django.contrib.auth import get_user_model

from common.models import TimestampedMetaModelMixin

from civic.choices import SuggestionStatusChoices

User = get_user_model()


class Suggestion(TimestampedMetaModelMixin):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="suggestions")
    status = models.CharField(
        choices=SuggestionStatusChoices.choices,
        max_length=150,
        default=SuggestionStatusChoices.REGISTERED,
    )
    description = models.TextField()

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "Suggestion"
        verbose_name_plural = "Suggestions"
