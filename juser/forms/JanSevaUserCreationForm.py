# -*- coding: utf-8 -*-

from django import forms
from juser.models import JanSevaUser


class JanSevaUserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput
    )

    def clean(self):
        super(JanSevaUserCreationForm, self).clean()
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match, Please enter again.")
        else:
            pass

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        else:
            pass
        return user

    class Meta:
        model = JanSevaUser
        fields = ("email", "username")
