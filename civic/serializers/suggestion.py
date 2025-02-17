# -*- coding: utf-8 -*-

from rest_framework import serializers

from civic.models import Suggestion


class SuggestionRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Suggestion
        fields = "__all__"


class SuggestionListSerializer(serializers.Serializer):

    uuid = serializers.UUIDField()
    full_name = serializers.CharField()
    status = serializers.CharField()
    description = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def get_description(self, obj):
        return obj["description"][:150]


class SuggestionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Suggestion
        exclude = ("is_deleted",)


class SuggestionStatusUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Suggestion
        fields = ("status",)
        read_only_fields = ("uuid",)
