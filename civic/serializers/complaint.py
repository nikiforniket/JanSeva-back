# -*- coding: utf-8 -*-


from rest_framework import serializers

from civic.models import Complaint


class ComplaintRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complaint
        fields = "__all__"
        read_only_fields = ("uuid",)


class ComplaintListSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    full_name = serializers.CharField()
    phone_number = serializers.CharField()
    department_name = serializers.CharField()
    category_name = serializers.CharField()
    status = serializers.CharField()
    location_name = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class ComplaintDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complaint
        exclude = ("is_deleted",)


class ComplaintStatusUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complaint
        fields = ("status",)
        read_only_fields = ("uuid",)
