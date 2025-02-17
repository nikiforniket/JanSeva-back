# -*- coding: utf-8 -*-
from django.db.models import F
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.pagination import ListPagination, SelectPagination

from legislator.models import Representative
from legislator.serializers import RepresentativeSelectSerializer


class RepresentativeSelectView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = RepresentativeSelectSerializer
    pagination_class = SelectPagination

    def get_queryset(self):
        return (
            Representative.objects.filter(is_deleted=False)
            .annotate(
                full_name=F("user__full_name"),
                constituency_name=F("constituency__name"),
            )
            .values("id", "full_name", "constituency_name")
        )

    def filter_queryset(self, queryset):
        search = self.request.query_params.get("search", None)
        if search:
            queryset = queryset.filter(full_name__icontains=search)
        return queryset
