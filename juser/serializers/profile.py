# -*- coding: utf-8 -*-

from rest_framework import serializers

from juser.models import JanSevaUserProfile


class JanSevaUserProfileSerializer(serializers.ModelSerializer):
    userid = serializers.IntegerField()
    phone_number = serializers.CharField()
    email = serializers.EmailField()
    full_name = serializers.CharField()

    class Meta:
        model = JanSevaUserProfile
        fields = (
            "id",
            "userid",
            "phone_number",
            "whatsapp_number",
            "dob",
            "location",
            "gender",
            "photo",
            "email",
            "full_name"
        )


class JanSevaUserProfileUpdateSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)

    def update(self, instance, validated_data):
        instance.user.email = validated_data.get("email", instance.user.email)
        instance.user.full_name = validated_data.get("full_name", instance.user.full_name)
        instance.user.save()
        validated_data.pop("email", None)
        validated_data.pop("full_name", None)
        super().update(instance, validated_data)

    class Meta:
        model = JanSevaUserProfile
        fields = (
            "email",
            "full_name",
            "whatsapp_number",
            "dob",
            "gender",
            "photo",
        )