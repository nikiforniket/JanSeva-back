# -*- coding: utf-8 -*-

from django.urls import path


from legislator.views import FundRegisterView, FundListView, FundDetailView, AllocationDetailView, AllocationListView, AllocationRegisterView

legislator_urlpatterns = [
    path("funds/", FundListView.as_view(), name="fund-list"),
    path("funds/register/", FundRegisterView.as_view(), name="fund-register"),
    path("funds/<int:pk>/", FundDetailView.as_view(), name="fund-detail"),
    path("allocations/", AllocationListView.as_view(), name="allocation-list"),
    path("allocations/register/", AllocationRegisterView.as_view(), name="allocation-register"),
    path("allocations/<int:pk>/", AllocationDetailView.as_view(), name="allocation-detail"),
]