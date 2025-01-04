# -*- coding: utf-8 -*-

from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError

class JUserManager(BaseUserManager):
    """User manager for users of JanSeva application"""

    def create_user(self, email, full_name, password, phone_number, create=True):
        if not email:
            raise ValidationError("Email is required.")
        if not full_name:
            raise ValidationError("Full name is required")
        if not password:
            raise ValidationError("Password is required.")
        if not phone_number:
            raise ValidationError("Phone number is required.")
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            phone_number=phone_number,
        )
        user.set_password(password)
        if create:
            user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password, phone_number):
        user = self.create_user(email, full_name, password, phone_number, create=False)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
