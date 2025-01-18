# -*- coding: utf-8 -*-


from rest_framework import serializers

from civic.models import GeoLocationComplaint


class GeoLocationComplaintRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeoLocationComplaint
        fields = "__all__"
        read_only_fields = ("uuid",)


class GeoLocationComplaintListSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    full_name = serializers.CharField()
    phone_number = serializers.CharField()
    complaint_type = serializers.CharField()
    lat = serializers.DecimalField(max_digits=9, decimal_places=6)
    long = serializers.DecimalField(max_digits=9, decimal_places=6)
    status = serializers.CharField()
    location_name = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class GeolocationComplaintDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeoLocationComplaint
        exclude = ("is_deleted",)


class GeolocationComplaintStatusUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeoLocationComplaint
        fields = ("status",)
        read_only_fields = ("uuid",)