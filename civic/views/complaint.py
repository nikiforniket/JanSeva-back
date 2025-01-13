# -*- coding: utf-8 -*-
from django.db.models import F
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.pagination import ListPagination
from civic.models import Complaint
from civic.serializers import (
    ComplaintRegisterSerializer,
    ComplaintListSerializer,
    ComplaintDetailSerializer,
)


class ComplaintRegisterView(generics.CreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = ComplaintRegisterSerializer

    def create(self, request, *args, **kwargs):
        try:
            request.data["user"] = request.user.id
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Complaint registered successfully."},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {
                        "message": "Please provide correct values for complaint registration.",
                        "errors": serializer.errors,
                        "error_code": 4003,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                {
                    "message": f"{e.__class__.__name__}",
                    "errors": [f"{e}"],
                    "error_code": 4002,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ComplaintListView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = ComplaintListSerializer
    pagination_class = ListPagination
    lookup_field = "uuid"

    def get_queryset(self):
        return (
            Complaint.objects.filter(is_deleted=False)
            .filter(is_deleted=False)
            .annotate(
                department_name=F("department__name"),
                category_name=F("category__name"),
                full_name=F("user__full_name"),
                number=F("user__phone_number"),
                location_name=F("location__name"),
            )
            .values(
                "uuid",
                "department_name",
                "category_name",
                "full_name",
                "number",
                "status",
                "location_name",
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


class ComplaintDetailView(generics.RetrieveAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = ComplaintDetailSerializer
    lookup_field = "uuid"

    def get_queryset(self):
        return Complaint.objects.filter(is_deleted=False)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.serializer_class(instance)
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
