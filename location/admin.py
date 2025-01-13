# -*- coding: utf-8 -*-

from django.contrib import admin

from location.models import State, Constituency, Block, LocalBody, SubLocalBody


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")


@admin.register(Constituency)
class ConstituencyAdmin(admin.ModelAdmin):
    list_display = ("no", "state", "name", "election_type")
    list_filter = ("state", "election_type")
    search_fields = ("name", "state__name")


@admin.register(LocalBody)
class LocalBodyAdmin(admin.ModelAdmin):
    list_display = ("name", "local_body_type", "block")
    list_filter = ("local_body_type", "block")
    search_fields = ("name",)


@admin.register(Block)
class BoothAdmin(admin.ModelAdmin):
    list_display = ("name", "constituency")
    list_filter = ("constituency",)
    search_fields = ("name",)


@admin.register(SubLocalBody)
class SubLocalBodyAdmin(admin.ModelAdmin):
    list_display = ("name", "local_body")
    search_fields = ("name",)
