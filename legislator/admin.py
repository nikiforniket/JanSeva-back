# -*- coding: utf-8 -*-

from django.contrib import admin

from legislator.models import Representative


@admin.register(Representative)
class RepresentativeAdmin(admin.ModelAdmin):
    pass