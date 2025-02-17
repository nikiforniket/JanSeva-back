# -*- coding: utf-8 -*-

from rest_framework import serializers


class RepresentativeSelectSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()