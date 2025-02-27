# -*- coding: utf-8 -*-

from django.contrib import admin

from news.models import News, NewsCategory

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "short_title", "category", "status", "created_at")
    list_filter = ("category", "status")
    search_fields = ("short_title",)


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_approved")
    list_filter = ("is_approved",)
    search_fields = ("name",)
