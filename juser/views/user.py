# -*- coding: utf-8 -*-
from django.db.models import F
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from juser.models import ElectProUserProfile
from juser.serializers.user import (
    RegisterUserSerializer,
    UpdateProfileSerializer,
    DetailProfileSerializer,
    ListProfileSerializer,
)
from juser.pagination import UserPagination


class UserRegisterView(generics.CreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "User registered successfully."},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {
                        "message": "Please provide correct values for user registration.",
                        "error": serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                {"message": f"{e.__class__.__name__} : {e}", "error_code": 1002},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class UserListView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]
    serializer_class = ListProfileSerializer
    pagination_class = UserPagination

    def get_queryset(self):
        return ElectProUserProfile.objects.annotate(
            booth_name=F("booth__name"),
            local_body_name=F("local_body__name"),
            constituency_name=F("constituency__name"),
        ).values(
            "full_name",
            "email",
            "phone_number",
            "age",
            "photo",
            "booth",
            "local_body",
            "constituency",
            "booth_name",
            "local_body_name",
            "constituency_name",
        )

    def filter_queryset(self, queryset):
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class UserDetailView(generics.RetrieveAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]
    serializer_class = DetailProfileSerializer

    def get_queryset(self):
        ElectProUserProfile.objects.values(
            "full_name",
            "email",
            "phone_number",
            "age",
            "photo",
            "booth",
            "local_body",
            "constituency",
        ).prefetch_related("docs")

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object())
        return Response(serializer.data)


class UserUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]
    serializer_class = UpdateProfileSerializer

    def update(self, request, *args, **kwargs):
        try:
            instance = request.user.profile
            serializer = self.serializer_class(data=request.data, instance=instance)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "User profile updated successfully."},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "message": "Please provide correct values for updating user.",
                        "error": serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                {"message": f"{e.__class__.__name__} : {e}", "error_code": 1003},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
