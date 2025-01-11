# -*- coding: utf-8 -*-


from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from civic.models import Department
from civic.serializers import DepartmentSerializer, DepartmentSelectSerializer, DepartmentDetailSerializer, \
    DepartmentUpdateSerializer


class DepartmentRegisterView(generics.CreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
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
                        "error": serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                {"message": f"{e.__class__.__name__} : {e}", "error_code": 2002},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class DepartmentSelectView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    serializer_class = DepartmentSelectSerializer

    def get_queryset(self):
        return Department.objects.filter(is_deleted=False)


class DepartmentUpdateDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]

    def get_queryset(self):
        return Department.objects.filter(is_deleted=False).prefetch_related("categories")

    def get_serializer_class(self):
        if self.request.method == "GET":
            return DepartmentDetailSerializer
        elif self.request.method in ["PATCH", "PUT"]:
            return DepartmentUpdateSerializer
