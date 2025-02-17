# -*- coding: utf-8 -*-

from rest_framework import serializers

from legislator.models import Fund, Allocation


class FundRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fund
        fields = "__all__"
        read_only_fields = ("id",)


class AllocationRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Allocation
        fields = "__all__"
        read_only_fields = ("id",)


class FundListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    amount = serializers.IntegerField()
    year = serializers.IntegerField()
    description = serializers.CharField()
    representative_name = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class AllocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Allocation
        fields = "__all__"
        read_only_fields = ("id",)


class FundDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fund
        fields = "__all__"
        read_only_fields = ("id",)


class FundUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fund
        fields = ("amount", "year", "description", "representative")
        read_only_fields = ("id",)


class AllocationUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Allocation
        fields = ("amount", "month_start", "month_end", "description")
        read_only_fields = ("id",)
