# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model

from rest_framework import serializers

from juser.models import ElectProUser
from juser.models import ElectProUserProfile
from juser.models import ElectProUserProfileDoc
from juser.choices import ProfileTypeChoices


User = get_user_model()


class UserMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElectProUser
        fields = ("id", "username", "date_joined")


class RegisterUserSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data["age"] < 18:
            raise serializers.ValidationError("User must be at least 18 years old.")
        if (
            data["profile_type"]
            in [
                ProfileTypeChoices.BOOTH_PRESIDENT,
                ProfileTypeChoices.BOOTH_VICE_PRESIDENT,
                ProfileTypeChoices.BOOTH_WORKERS,
            ]
            and not data["booth"]
        ):
            raise serializers.ValidationError(
                f"Booth is required for {ProfileTypeChoices.get_label(data['profile_type'])}."
            )
        if (
            data["profile_type"] == ProfileTypeChoices.LOCAL_BODY_INCHARGE
            and not data["local_body"]
        ):
            raise serializers.ValidationError(
                f"Local body is required for {ProfileTypeChoices.get_label(data['profile_type'])}."
            )
        if data["profile_type"] == ProfileTypeChoices.WOMEN_WING_INCHARGE and not (
            data["local_body"] or data["constituency"] or data["booth"]
        ):
            raise serializers.ValidationError(
                f"Local body, constituency or booth is required for {ProfileTypeChoices.get_label(data['profile_type'])}."
            )
        return data

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            full_name=validated_data["full_name"],
            phone_number=validated_data["phone_number"],
        )
        user.save()
        validated_data["user"] = user
        profile = ElectProUser.objects.create_user(**validated_data)
        return profile

    class Meta:
        model = ElectProUserProfile
        fields = "__all__"
        exclude = ("user",)


class UpdateProfileSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data["age"] < 18:
            raise serializers.ValidationError("User must be at least 18 years old.")
        if (
            data["profile_type"]
            in [
                ProfileTypeChoices.BOOTH_PRESIDENT,
                ProfileTypeChoices.BOOTH_VICE_PRESIDENT,
                ProfileTypeChoices.BOOTH_WORKERS,
            ]
            and not data["booth"]
        ):
            raise serializers.ValidationError(
                f"Booth is required for {ProfileTypeChoices.get_label(data['profile_type'])}."
            )
        if (
            data["profile_type"] == ProfileTypeChoices.LOCAL_BODY_INCHARGE
            and not data["local_body"]
        ):
            raise serializers.ValidationError(
                f"Local body is required for {ProfileTypeChoices.get_label(data['profile_type'])}."
            )
        if data["profile_type"] == ProfileTypeChoices.WOMEN_WING_INCHARGE and not (
            data["local_body"] or data["constituency"] or data["booth"]
        ):
            raise serializers.ValidationError(
                f"Local body, constituency or booth is required for {ProfileTypeChoices.get_label(data['profile_type'])}."
            )

        return data

    def update(self, instance, validated_data):
        instance.user.email = validated_data["email"]
        instance.user.phone_number = validated_data["phone_number"]
        instance.user.full_name = validated_data["full_name"]
        instance.user.save()
        instance.whatsapp_number = validated_data["phone_number"]
        super().update(instance, validated_data)

    class Meta:
        model = ElectProUserProfile
        fields = (
            "full_name",
            "email",
            "phone_number",
            "whatsapp_number",
            "age",
            "voter_id",
            "aadhar_id",
            "photo",
            "booth",
            "local_body",
            "constituency",
        )


class ListProfileSerializer(serializers.ModelSerializer):
    user = UserMetaSerializer(read_only=True)

    class Meta:
        model = ElectProUserProfile
        fields = (
            "id",
            "full_name",
            "email",
            "phone_number",
            "profile_type",
            "age",
            "photo",
            "booth_name",
            "local_body_name",
            "constituency_name",
        )


class ProfileDocsMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElectProUserProfileDoc
        fields = ("id", "file", "doc_type")


class DetailProfileSerializer(serializers.ModelSerializer):
    docs = ProfileDocsMetaSerializer(many=True, read_only=True)
    user = UserMetaSerializer(read_only=True)

    class Meta:
        model = ElectProUserProfile
        fields = "__all__"
