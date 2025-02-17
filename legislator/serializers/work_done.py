# -*- coding: utf-8 -*-

from rest_framework import serializers

from legislator.models import WorkDone


class WorkDoneRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkDone
        fields = "__all__"
        read_only_fields = ("id",)


class WorkDoneListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    representative_name = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
