# -*- coding: utf-8 -*-

import uuid
import re

from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core import validators
from juser.managers import JUserManager


class JanSevaUser(AbstractUser, PermissionsMixin):
    """
    User model for electoral application
    Required Fields :: (email, full_name)
    """

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    username = models.CharField(
        _("user name"),
        max_length=32,
        unique=True,
        null=True,
        blank=True,
        help_text="Required. 30 characters or fewer. Letters, numbers and /./-/_characters",
        validators=[
            validators.RegexValidator(
                re.compile(r"^[\w.-]+$"), _("Enter a valid username."), "invalid"
            )
        ],
    )
    email = models.EmailField(
        _("email"), max_length=320, null=True, blank=True, unique=True
    )
    full_name = models.CharField(_("full name"), max_length=256, blank=False)
    is_superuser = models.BooleanField(
        default=False,
        verbose_name="superuser status",
        help_text="Designates whether the user can have access"
        "to all permissions on every model.",
    )
    is_active = models.BooleanField(
        _("active status"),
        default=True,
        help_text="Designates whether this user should be treated as active."
        "Unselect this instead of deleting accounts.",
    )
    is_admin = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(
        _("email verification status"),
        default=True,
        help_text="Designates whether this user email is verified.",
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_deleted = models.BooleanField(
        _("deleted status"),
        default=False,
        help_text="Designates whether the user is soft deleted.",
    )
    full_name = models.CharField(_("full name"), max_length=256, blank=True)
    phone_number = models.CharField(
        _("Phone number of User"), max_length=13, blank=False, null=False, unique=True
    )
    date_joined = models.DateTimeField(
        verbose_name="date/time joined at", default=timezone.now
    )
    last_login_at = models.DateTimeField(
        verbose_name="last logged in at", null=True, blank=True
    )

    objects = JUserManager()

    EMAIL_FIELD = "phone_number"
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["full_name",]

    def __str__(self):
        return f"{self.full_name} -> {self.email}"

    class Meta:
        verbose_name = "JanSeva User"
        verbose_name_plural = "JanSeva Users"
        ordering = ["full_name", "-date_joined"]
