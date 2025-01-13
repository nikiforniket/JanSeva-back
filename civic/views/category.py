# -*- coding: utf-8 -*-


from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.pagination import SelectPagination

from civic.serializers import CategorySerializer
from civic.serializers import CategorySelectSerializer
from civic.serializers import CategoryUpdateSerializer

from civic.models import Category


class CategoryRegisterView(generics.CreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Category registered successfully."},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {
                        "message": "Please provide correct values for category registration.",
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


class CategoryUpdateView(generics.UpdateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = CategoryUpdateSerializer

    def get_queryset(self):
        return Category.objects.filter(is_deleted=False)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.serializer_class(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Category updated successfully."},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "message": "Please provide correct values for category update.",
                        "error": serializer.errors,
                        "error_code": 3003,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                {"message": f"{e.__class__.__name__} : {e}", "error_code": 3002},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class CategorySelectView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = CategorySelectSerializer
    pagination_class = SelectPagination

    def get_queryset(self):
        return Category.objects.filter(is_deleted=False)

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return queryset.filter(department_id=self.kwargs.get("department_id"))
