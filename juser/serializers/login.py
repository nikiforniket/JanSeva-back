# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404

from rest_framework import serializers

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        user = get_object_or_404(User, phone_number=attrs["phone_number"])
        if not check_password(attrs["password"], user.password):
            raise serializers.ValidationError({"password": "Invalid password"})
        return attrs
