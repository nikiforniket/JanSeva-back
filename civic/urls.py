# -*- coding: utf-8 -*-

from django.urls import path

from civic.views import (
    CategorySelectView,
    CategoryUpdateView,
    CategoryRegisterView,
    DepartmentSelectView,
    DepartmentUpdateDetailView,
    DepartmentRegisterView,
)


civic_urlpatterns = [
    path("departments/", DepartmentRegisterView.as_view(), name="department-register"),
    path(
        "departments/<int:pk>/",
        DepartmentUpdateDetailView.as_view(),
        name="department-update",
    ),
    path(
        "departments/select/", DepartmentSelectView.as_view(), name="department-select"
    ),
    path("categories/", CategoryRegisterView.as_view(), name="category-register"),
    path("categories/<int:pk>/", CategoryUpdateView.as_view(), name="category-update"),
    path("categories/select/", CategorySelectView.as_view(), name="category-select"),
]
