# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from news.models.news import News
from news.choices import NewStatusChoices
from news.serializers.news import FlashNewsSerializer


class FlashNewsView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FlashNewsSerializer

    def get_queryset(self):
        return News.objects.filter(status=NewStatusChoices.ACTIVE).order_by("-created_at")[:5]