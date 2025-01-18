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
    DemandLetterRegisterView,
    DemandLetterListView,
    DemandLetterDetailView,
    SuggestionRegisterView,
    SuggestionListView,
    SuggestionDetailView
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
    path(
        "demand-letters/register/",
        DemandLetterRegisterView.as_view(),
        name="demand-letter-register",
    ),
    path(
        "demand-letters/",
        DemandLetterListView.as_view(),
        name="demand-letter-list",
    ),
    path(
        "demand-letters/<uuid:uuid>/",
        DemandLetterDetailView.as_view(),
        name="demand-letter-detail",
    ),
    path(
        "suggestions/register/",
        SuggestionRegisterView.as_view(),
        name="suggestions-register"
    ),
    path(
        "suggestions",
        SuggestionListView.as_view(),
        name="suggestions"
    ),
    path(
        "suggestions/<uuid:uuid>/",
        SuggestionDetailView.as_view(),
        name="suggestions-detail"
    )
]
