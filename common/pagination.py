from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class ListPagination(PageNumberPagination):

    # Set the maximum limit a client can request
    page_size = 30


class SelectPagination(LimitOffsetPagination):
    # Set the default limit
    default_limit = 20  # Default number of items per page

    # Set the maximum limit a client can request
    max_limit = 30

    # Override the offset query parameter name
    offset_query_param = "start"

    # Override the limit query parameter name
    limit_query_param = "items"
