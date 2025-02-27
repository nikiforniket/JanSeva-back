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
    fund_year = serializers.IntegerField()
    fund_month_start = serializers.IntegerField()
    fund_month_end = serializers.IntegerField()
    allocated_fund = serializers.IntegerField()
    location_name = serializers.CharField()
    location_parent_name = serializers.CharField()
    location_parent_type = serializers.CharField()
    scheme_name = serializers.CharField()
    sector_name = serializers.CharField()
    scheme = serializers.CharField()
    amount = serializers.IntegerField()
    description = serializers.CharField()
    year = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class WorkDoneUpdateSerializer(serializers.ModelSerializer):
    location_parent = serializers.IntegerField(read_only=True)

    class Meta:
        model = WorkDone
        fields = ("id", "fund", "sector", "scheme", "amount", "location_parent", "location", "description", "year")
        read_only_fields = ("id",)
