# -*- coding: utf-8 -*-
from django.db.models import F
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from civic.models import Suggestion
from common.pagination import ListPagination

from civic.serializers import (
    SuggestionRegisterSerializer,
    SuggestionListSerializer,
    SuggestionDetailSerializer,
    SuggestionStatusUpdateSerializer,
)


class SuggestionRegisterView(generics.CreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = SuggestionRegisterSerializer

    def create(self, request, *args, **kwargs):
        try:
            request.data["user"] = request.user.id
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Suggestion registered successfully."},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {
                        "message": "Please provide correct values for suggestion registration.",
                        "errors": serializer.errors,
                        "error_code": 2003,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                {
                    "message": f"{e.__class__.__name__}",
                    "errors": [f"{e}"],
                    "error_code": 2002,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class SuggestionListView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = SuggestionListSerializer
    pagination_class = ListPagination

    def get_queryset(self):
        return (
            Suggestion.objects.filter(is_deleted=False)
            .annotate(
                full_name=F("user__full_name"), phone_number=F("user__phone_number")
            )
            .values(
                "uuid",
                "full_name",
                "phone_number",
                "status",
                "description",
                "created_at",
                "updated_at",
            )
        )

    def filter_queryset(self, queryset):
        return queryset

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.serializer_class(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {
                    "message": f"{e.__class__.__name__}",
                    "errors": [f"{e}"],
                    "error_code": 4001,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class SuggestionDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_field = "uuid"

    def get_queryset(self):
        return Suggestion.objects.filter(is_deleted=False)

    def get_serializer_class(self):
        if self.request.method in ["PATCH"]:
            return SuggestionStatusUpdateSerializer
        else:
            return SuggestionDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer_class()(instance)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {
                    "message": f"{e.__class__.__name__}",
                    "errors": [f"{e}"],
                    "error_code": 4001,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
