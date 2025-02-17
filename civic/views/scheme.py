# -*- coding: utf-8 -*-


from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.pagination import ListPagination, SelectPagination
from civic.models import Scheme
from civic.serializers import (
    SchemeRegisterSerializer,
    SchemeListSerializer,
    SchemeDetailSerializer,
    SchemeUpdateSerializer,
    SchemeSelectSerializer
)


class SchemeRegisterView(generics.CreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = SchemeRegisterSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Scheme registered successfully."},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {
                        "message": "Please provide correct values for scheme registration.",
                        "errors": serializer.errors,
                        "error_code": 3003,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                {
                    "message": f"{e.__class__.__name__}",
                    "errors": [f"{e}"],
                    "error_code": 3002,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class SchemeSelectView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = SchemeSelectSerializer
    pagination_class = SelectPagination

    def get_queryset(self):
        return Scheme.objects.filter(is_deleted=False)

    def filter_queryset(self, queryset):
        search = self.request.query_params.get("search", None)
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset


class SchemeListView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = SchemeListSerializer
    pagination_class = ListPagination

    def get_queryset(self):
        return Scheme.objects.filter(is_deleted=False).values(
            "id",
            "name",
            "sector",
            "year",
            "is_active",
            "created_at",
            "updated_at"
        )


class SchemeDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Scheme.objects.filter(is_deleted=False)

    def get_serializer_class(self):
        if self.request.method in ["PATCH"]:
            return SchemeUpdateSerializer
        return SchemeUpdateSerializer
