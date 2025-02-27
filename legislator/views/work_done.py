# -*- coding: utf-8 -*-
from django.db.models import F
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.pagination import ListPagination, SelectPagination

from legislator.models import WorkDone

from legislator.serializers import WorkDoneRegisterSerializer, WorkDoneListSerializer, WorkDoneUpdateSerializer


class WorkDoneRegisterView(generics.CreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = WorkDoneRegisterSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Work done registered successfully."},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {
                        "message": "Please provide correct values for work done registration.",
                        "errors": serializer.errors,
                        "error_code": 4003,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except ValidationError as e:
            return Response(
                {
                    "message": f"{e.__class__.__name__}",
                    "errors": [f"{e}"],
                    "error_code": 4002,
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


class WorkDoneListView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = WorkDoneListSerializer
    pagination_class = ListPagination
    queryset = WorkDone.objects.filter(is_deleted=False).annotate(
        fund_year=F("fund__fund__year"),
        fund_month_start=F("fund__month_start"),
        fund_month_end=F("fund__month_end"),
        allocated_fund=F("fund__amount"),
        location_name=F("location__name"),
        location_parent_name=F("location__local_body__name"),
        location_parent_type=F("location__local_body__local_body_type"),
        scheme_name=F("scheme__name"),
        sector_name=F("sector__name"),
    )


class WorkDoneDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = WorkDone.objects.filter(is_deleted=False).annotate(
        location_parent=F("location__local_body_id"),
    )

    def get_serializer_class(self):
        return WorkDoneUpdateSerializer
