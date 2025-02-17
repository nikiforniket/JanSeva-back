# -*- coding: utf-8 -*-
from django.db.models import F
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.pagination import ListPagination
from civic.models import DemandLetter
from civic.serializers import (
    DemandLetterRegisterSerializer,
    DemandLetterListSerializer,
    DemandLetterDetailSerializer,
    DemandLetterStatusUpdateSerializer,
)


class DemandLetterRegisterView(generics.CreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = DemandLetterRegisterSerializer

    def create(self, request, *args, **kwargs):
        try:
            request.data["user"] = request.user.id
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Demand Letter registered successfully."},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {
                        "message": "Please provide correct values for demand letter registration.",
                        "errors": serializer.errors,
                        "error_code": 5003,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                {
                    "message": f"{e.__class__.__name__}",
                    "errors": [f"{e}"],
                    "error_code": 5002,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class DemandLetterListView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = DemandLetterListSerializer
    pagination_class = ListPagination

    def get_queryset(self):
        return (
            DemandLetter.objects.filter(is_deleted=False)
            .annotate(
                full_name=F("user__full_name"),
                phone_number=F("user__phone_number"),
            )
            .values(
                "uuid",
                "full_name",
                "phone_number",
                "status",
                "subject",
                "description",
                "created_at",
                "updated_at",
            )
        )


class DemandLetterDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = DemandLetterDetailSerializer
    lookup_field = "uuid"

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return DemandLetterStatusUpdateSerializer
        return self.serializer_class

    def get_queryset(self):
        return DemandLetter.objects.filter(is_deleted=False)

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
