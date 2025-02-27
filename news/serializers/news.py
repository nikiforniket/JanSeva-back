# -*- coding: utf-8 -*-

from rest_framework import serializers

from news.models.news import News
from news.models.news_category import NewsCategory

class FlashNewsSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    short_title = serializers.CharField()
    short_content = serializers.CharField()
    title_image = serializers.FileField()