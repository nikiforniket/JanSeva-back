# -*- coding: utf-8 -*-

from rest_framework import serializers

from civic.models import Department
from civic.serializers.category import CategoryMetaSerializer


class DepartmentSelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ("id", "name")


class DepartmentListSerializer(DepartmentSelectSerializer): ...


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ("id", "name")
        read_only_fields = ("id",)


class DepartmentDetailSerializer(serializers.ModelSerializer):
    categories = CategoryMetaSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ("id", "name", "categories")
        read_only_fields = ("id",)


class DepartmentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ("name",)
        read_only_fields = ("id",)
