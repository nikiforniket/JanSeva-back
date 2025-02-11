# -*- coding: utf-8 -*-

from rest_framework import serializers

from civic.models import GeoLocationComplaint, GeoLocationComplaintFiles


class GeoLocationComplaintFilesRegisterSerializer(serializers.ModelSerializer):

        class Meta:
            model = GeoLocationComplaintFiles
            fields = "__all__"
            read_only_fields = ("id",)


class GeoLocationComplaintRegisterSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     files = validated_data.pop("files")
    #
    #     complaint = super().create(validated_data)

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
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class GeolocationComplaintFilesMetaSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    def get_file(self, obj):
        return "https://media.tegna-media.com/assets/WBNS/images/e35862b5-c76e-4191-bfc9-828403950e94/e35862b5-c76e-4191-bfc9-828403950e94_1920x1080.jpg"

    class Meta:
        model = GeoLocationComplaintFiles
        fields = ("id", "file",)


class GeolocationComplaintDetailSerializer(serializers.ModelSerializer):
    files = GeolocationComplaintFilesMetaSerializer(many=True)

    class Meta:
        model = GeoLocationComplaint
        exclude = ("is_deleted",)


class GeolocationComplaintStatusUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeoLocationComplaint
        fields = ("status",)
        read_only_fields = ("uuid",)
