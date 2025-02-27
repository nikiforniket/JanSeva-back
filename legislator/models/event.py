# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin
from location.models import SubLocalBody, LocalBody

class Event(TimestampedMetaModelMixin):

    title = models.CharField(max_length=255, unique=True)
    event_date = models.DateField()
    event_header_photo = models.FileField(upload_to="event_header_photos/")
    event_description = models.TextField()
    location = models.ForeignKey(
        LocalBody,
        related_name="events",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    sub_location = models.ForeignKey(
        SubLocalBody,
        related_name="events",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.title} | {self.event_date}"

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["title", "-event_date"]