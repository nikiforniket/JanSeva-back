# -*- coding: utf-8 -*-

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from juser.views import LoginView, RegisterUserSerializer, JanSevaUserProfileView


juser_urls = [
    path("register/", RegisterUserSerializer.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", JanSevaUserProfileView.as_view(), name="profile"),
]
