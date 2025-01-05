# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import get_user_model

from common.models import TimestampedMetaModelMixin
from juser.choices import ProfileTypeChoices, ProfileTypeDocsChoices


User = get_user_model()


class JanSevaUserProfile(TimestampedMetaModelMixin):

    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE, null=True, blank=True
    )
    profile_type = models.CharField(choices=ProfileTypeChoices.choices, max_length=10)
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=13)
    whatsapp_number = models.CharField(max_length=13)
    age = models.PositiveIntegerField()
    voter_id = models.CharField(max_length=50, unique=True)
    voter_id_is_verified = models.BooleanField(default=False)
    aadhar_id = models.CharField(max_length=50)
    aadhar_id_is_verified = models.BooleanField(default=False)
    photo = models.FileField(upload_to="users/profile/picture")
    booth = models.ForeignKey(
        Booth,
        related_name="user_profiles",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    local_body = models.ForeignKey(
        LocalBody,
        related_name="user_profiles",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    constituency = models.ForeignKey(
        Constituency,
        related_name="user_profiles",
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
