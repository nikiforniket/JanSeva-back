# -*- coding: utf-8 -*-

from django.urls import path

from location.views import LocalBodySelectView, SubLocalBodySelectView, BlockSelectView


location_urlpatterns = [
    path("blocks/select/", BlockSelectView.as_view(), name="block-select"),
    path(
        "local-bodies/select/", LocalBodySelectView.as_view(), name="local-body-select"
    ),
    path(
        "sub-local-bodies/select/",
        SubLocalBodySelectView.as_view(),
        name="sub-local-body-select",
    ),
]
