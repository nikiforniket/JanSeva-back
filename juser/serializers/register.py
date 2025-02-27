# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model

from juser.models import JanSevaUserProfile

from rest_framework import serializers

from location.models import SubLocalBody

User = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    dob = serializers.DateField(required=True)
    gender = serializers.CharField(required=True)
    # location = serializers.PrimaryKeyRelatedField(queryset=SubLocalBody.objects.filter(is_deleted=False), required=True)
    whatsapp_number = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ("id", "phone_number", "password", "full_name",
                  "email", "dob", "gender", "whatsapp_number")
        read_only_fields = ("id",)

    def create(self, validated_data):
        phone_number = validated_data["phone_number"]
        whatsapp_number = validated_data.pop("whatsapp_number", phone_number)
        email = validated_data.pop("email", None)
        full_name = validated_data["full_name"]
        dob = validated_data["dob"]
        gender = validated_data["gender"]
        # location = validated_data["location"]
        user_data = {
            "phone_number": phone_number,
            "full_name": full_name,
            "email": email,
            "password": validated_data["password"],
        }
        user = User.objects.create_user(**user_data)
        user.set_password(validated_data["password"])
        JanSevaUserProfile.objects.create(
            user=user, whatsapp_number=whatsapp_number,
            dob=dob, gender=gender,
            # location=location
        )
        return user