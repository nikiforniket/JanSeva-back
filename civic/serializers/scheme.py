# -*- coding: utf-8 -*-

from rest_framework import serializers

from civic.models import Scheme


class SchemeRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scheme
        fields = "__all__"
        read_only_fields = ("id",)


class SchemeSelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scheme
        fields = ("id", "name",)


class SchemeListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    sector = serializers.CharField()
    year = serializers.IntegerField()
    is_active = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class SchemeDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scheme
        fields = ("id", "name", "sector", "year", "is_active", "created_at", "updated_at")
        read_only_fields = ("id",)


class SchemeUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scheme
        fields = ("id", "name", "sector", "year", "is_active")
        read_only_fields = ("id",)
