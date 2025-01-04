# -*- coding: utf-8 -*-

from django.db import models


class JanSevaTextChoices(models.TextChoices):

    @classmethod
    def get_label(cls, value):
        try:
            return cls(value).label
        except ValueError:
            return None