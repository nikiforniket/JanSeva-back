# -*- coding: utf-8 -*-

from rest_framework import serializers

from legislator.models import Event


class EventRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ("id",)


class EventListSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    event_date = serializers.DateField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()