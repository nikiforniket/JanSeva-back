# -*- coding: utf-8 -*-

from django.urls import path


from legislator.views import (
    FundRegisterView,
    FundListView,
    FundDetailView,
    AllocationDetailView,
    AllocationListView,
    AllocationRegisterView,
    AllocationSelectView,
    RepresentativeSelectView,
    WorkDoneRegisterView,
    WorkDoneListView,
    WorkDoneDetailView
)

legislator_urlpatterns = [
    path("funds/", FundListView.as_view(), name="fund-list"),
    path("funds/register/", FundRegisterView.as_view(), name="fund-register"),
    path("funds/<int:pk>/", FundDetailView.as_view(), name="fund-detail"),
    path("allocations/", AllocationListView.as_view(), name="allocation-list"),
    path(
        "allocations/register/",
        AllocationRegisterView.as_view(),
        name="allocation-register",
    ),
    path(
        "allocations/<int:pk>/",
        AllocationDetailView.as_view(),
        name="allocation-detail",
    ),
    path(
        "allocations/select/",
        AllocationSelectView.as_view(),
        name="allocation-select",
    ),
    path(
        "representatives/select/",
        RepresentativeSelectView.as_view(),
        name="representative-select",
    ),
    path("works-done/register/", WorkDoneRegisterView.as_view(), name="work-done-register"),
    path("works-done/", WorkDoneListView.as_view(), name="work-done-list"),
    path("works-done/<int:pk>/", WorkDoneDetailView.as_view(), name="works-done-detail")
]
