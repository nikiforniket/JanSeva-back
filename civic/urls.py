# -*- coding: utf-8 -*-

from django.urls import path

from civic.views import (
    CategorySelectView,
    CategoryUpdateView,
    CategoryRegisterView,
    DepartmentSelectView,
    DepartmentUpdateDetailView,
    DepartmentRegisterView,
    DepartmentListView,
    ComplaintRegisterView,
    ComplaintListView,
    ComplaintDetailView,
)


civic_urlpatterns = [
    path("departments/", DepartmentListView.as_view(), name="department-list"),
    path(
        "departments/register/",
        DepartmentRegisterView.as_view(),
        name="department-register",
    ),
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
    path(
        "complaints/register/",
        ComplaintRegisterView.as_view(),
        name="complaint-register",
    ),
    path(
        "complaints/",
        ComplaintListView.as_view(),
        name="complaint-list",
    ),
    path(
        "complaints/<uuid:uuid>/",
        ComplaintDetailView.as_view(),
        name="complaint-detail",
    ),
]
