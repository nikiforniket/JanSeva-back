# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedMetaModelMixin

from news.models.news_category import NewsCategory
from news.choices import NewStatusChoices


class News(TimestampedMetaModelMixin):

    category = models.ForeignKey(
        NewsCategory, related_name="news", on_delete=models.CASCADE
    )
    short_title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=400)
    title_image = models.FileField(upload_to="news/title_images/")
    long_title = models.CharField(max_length=250)
    long_content = models.TextField()
    status = models.CharField(
        choices=NewStatusChoices.choices, default=NewStatusChoices.CREATED
    )

    def __str__(self):
        return f"{self.id} | {self.category} | {self.status} | {self.short_title}"

    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"
