# -*- coding: utf-8 -*-

from rest_framework import serializers

from location.models import LocalBody, SubLocalBody, Block


class BlockSelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Block
        fields = (
            "id",
            "name",
        )


class LocalBodySelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocalBody
        fields = (
            "id",
            "name",
        )


class SubLocalBodySelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubLocalBody
        fields = (
            "id",
            "name",
        )
