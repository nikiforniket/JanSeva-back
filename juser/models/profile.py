# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import get_user_model

from common.models import TimestampedMetaModelMixin
from location.models import SubLocalBody
from juser.choices import ProfileTypeChoices, ProfileTypeDocsChoices, GenderChoices

User = get_user_model()


class JanSevaUserProfile(TimestampedMetaModelMixin):

    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE, null=True, blank=True
    )
    profile_type = models.CharField(choices=ProfileTypeChoices.choices, max_length=10)
    whatsapp_number = models.CharField(max_length=13)
    dob = models.DateField()
    gender = models.CharField(choices=GenderChoices.choices, max_length=2)
    voter_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    voter_id_is_verified = models.BooleanField(default=False)
    aadhar_id = models.CharField(max_length=50, null=True, blank=True)
    aadhar_id_is_verified = models.BooleanField(default=False)
    photo = models.FileField(upload_to="users/profile/picture")
    location = models.ForeignKey(
        SubLocalBody,
        related_name="users",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.profile_type} | {self.user}"

    class Meta:
        verbose_name = "ElectProUser Profile"
        verbose_name_plural = "ElectProUser Profiles"


class JanSevaUserProfileDoc(TimestampedMetaModelMixin):

    profile = models.ForeignKey(
        JanSevaUserProfile, related_name="docs", on_delete=models.CASCADE
    )
    file = models.FileField(upload_to="user/profile/docs")
    doc_type = models.CharField(choices=ProfileTypeDocsChoices.choices, max_length=5)

    def __str__(self):
        return f"{self.doc_type} | {self.profile}"

    class Meta:
        verbose_name = "ElectProUser Profile Doc"
        verbose_name_plural = "ElectProUser Profile Docs"
