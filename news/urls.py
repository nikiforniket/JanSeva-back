# -*- coding: utf-8 -*-

from django.urls import path

from news.views import FlashNewsView

news_urlpatterns = [
    path("flash-news/", FlashNewsView.as_view(), name="flash-news"),
]
