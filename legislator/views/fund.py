# -*- coding: utf-8 -*-
from django.db.models import F
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.pagination import ListPagination, SelectPagination
from legislator.models import Fund, Allocation
from legislator.serializers import FundRegisterSerializer, FundListSerializer, FundDetailSerializer, FundUpdateSerializer, AllocationRegisterSerializer, AllocationSerializer, AllocationUpdateSerializer


class FundRegisterView(generics.CreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = FundRegisterSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Fund registered successfully."},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {
                        "message": "Please provide correct values for fund registration.",
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


class FundListView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = FundListSerializer
    pagination_class = ListPagination

    def get_queryset(self):
        return Fund.objects.filter(is_deleted=False).annotate(representative_name=F(
            'representative__user__full_name'
        )).values(
            "id",
            "representative_name",
            "description",
            "year",
            "amount",
            "created_at",
            "updated_at"
        )


class FundDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Fund.objects.filter(is_deleted=False)

    def get_serializer_class(self):
        if self.request.method in ["PATCH"]:
            return FundUpdateSerializer
        return FundDetailSerializer


class AllocationRegisterView(generics.CreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = AllocationRegisterSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Allocation registered successfully."},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {
                        "message": "Please provide correct values for allocation registration.",
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


class AllocationListView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = AllocationSerializer

    def get_queryset(self):
        return Allocation.objects.filter(is_deleted=False)

    def filter_queryset(self, queryset):
        fund = self.request.query_params.get("fund", None)
        if fund:
            queryset = queryset.filter(fund_id=fund)
            return queryset
        return queryset.none()


class AllocationDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Allocation.objects.filter(is_deleted=False)

    def get_serializer_class(self):
        if self.request.method in ["PATCH"]:
            return AllocationUpdateSerializer
        return AllocationSerializer