# -*- coding: utf-8 -*-


from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.pagination import ListPagination, SelectPagination
from civic.models import Sector
from civic.serializers import (
    DepartmentSerializer,
    DepartmentSelectSerializer,
    DepartmentDetailSerializer,
    DepartmentUpdateSerializer,
    DepartmentListSerializer,
)


class DepartmentRegisterView(generics.CreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = DepartmentSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Department registered successfully."},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {
                        "message": "Please provide correct values for department registration.",
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


class DepartmentSelectView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = DepartmentSelectSerializer
    pagination_class = SelectPagination

    def get_queryset(self):
        return Sector.objects.filter(is_deleted=False)


class DepartmentListView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = DepartmentListSerializer
    pagination_class = ListPagination

    def get_queryset(self):
        return Sector.objects.filter(is_deleted=False).prefetch_related(
            "categories"
        )


class DepartmentUpdateDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Sector.objects.filter(is_deleted=False).prefetch_related(
            "categories"
        )

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DepartmentDetailSerializer
        elif self.request.method in ["PATCH", "PUT"]:
            return DepartmentUpdateSerializer
