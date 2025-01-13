# -*- coding: utf-8 -*-

from rest_framework import serializers

from civic.models import DemandLetter


class DemandLetterRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = DemandLetter
        fields = "__all__"
        read_only_fields = ("uuid",)


class DemandLetterListSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    full_name = serializers.CharField()
    phone_number = serializers.CharField()
    status = serializers.CharField()
    subject = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class DemandLetterDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = DemandLetter
        exclude = ("is_deleted",)