# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from juser.models import JanSevaUser


class JanSevaUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=(
            "Django does not stores password in readable form,"
            "So you cannot see this user's password,"
            "but you can change the password "
            'using <a href="../password/">this form</a>.'
        ),
    )

    class Meta:
        model = JanSevaUser
        fields = ("email", "password")

    def clean_password(self):
        return self.initial["password"]
