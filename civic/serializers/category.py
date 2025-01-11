# -*- coding: utf-8 -*-

from rest_framework import serializers

from civic.models import Category


class CategoryMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("id", "name")


class CategorySelectSerializer(CategoryMetaSerializer): ...


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ("id",)
