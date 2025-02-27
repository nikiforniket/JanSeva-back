# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.db.models import F
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics

from juser.serializers import JanSevaUserProfileSerializer, JanSevaUserProfileUpdateSerializer
from juser.models import JanSevaUserProfile

User = get_user_model()


class JanSevaUserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return JanSevaUserProfileUpdateSerializer
        return JanSevaUserProfileSerializer

    def get_queryset(self):
        return JanSevaUserProfile.objects.filter(user=self.request.user).annotate(
            userid=F("user__id"),
            full_name=F("user__full_name"),
            phone_number=F("user__phone_number"),
            email=F("user__email")
        )

    def get_object(self):
        return get_object_or_404(self.get_queryset(), user=self.request.user)
