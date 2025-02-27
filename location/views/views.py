# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from common.pagination import SelectPagination

from location.models import LocalBody, SubLocalBody, Block

from location.serializers import (
    LocalBodySelectSerializer,
    SubLocalBodySelectSerializer,
    BlockSelectSerializer,
)


class BlockSelectView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = BlockSelectSerializer
    pagination_class = SelectPagination

    def get_queryset(self):
        return Block.objects.filter(is_deleted=False).values("id", "name")

    def filter_queryset(self, queryset):
        search = self.request.query_params.get("search", None)
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset


class LocalBodySelectView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = LocalBodySelectSerializer
    pagination_class = SelectPagination

    def get_queryset(self):
        return LocalBody.objects.filter(is_deleted=False).values("id", "name")

    def filter_queryset(self, queryset):
        search = self.request.query_params.get("search", None)
        local_body_type = self.request.query_params.get("local_body_type", None)
        if search:
            queryset = queryset.filter(name__icontains=search)
        if local_body_type:
            queryset = queryset.filter(local_body_type=local_body_type)
        return queryset


class SubLocalBodySelectView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = SubLocalBodySelectSerializer
    pagination_class = SelectPagination

    def get_queryset(self):
        return SubLocalBody.objects.filter(is_deleted=False).values("id", "name")

    def filter_queryset(self, queryset):
        search = self.request.query_params.get("search", None)
        local_body = self.request.query_params.get("local_body", None)
        if search:
            queryset = queryset.filter(name__icontains=search)
        if local_body:
            queryset = queryset.filter(local_body=local_body)
        else:
            queryset = queryset.none()
        return queryset
