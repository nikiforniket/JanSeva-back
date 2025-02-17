# -*- coding: utf-8 -*-

from rest_framework import serializers

from civic.models import Sector
from civic.serializers.category import CategoryMetaSerializer


class DepartmentSelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = ("id", "name",)


class DepartmentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = ("id", "name", "created_at", "updated_at")


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = ("id", "name")
        read_only_fields = ("id",)


class DepartmentDetailSerializer(serializers.ModelSerializer):
    categories = CategoryMetaSerializer(many=True, read_only=True)

    class Meta:
        model = Sector
        fields = ("id", "name", "categories", "created_at", "updated_at")
        read_only_fields = ("id",)


class DepartmentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector
        fields = ("name",)
        read_only_fields = ("id",)
