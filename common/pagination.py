from rest_framework.pagination import LimitOffsetPagination


class ListPagination(LimitOffsetPagination):
    # Set the default limit
    default_limit = 15  # Default number of items per page

    # Set the maximum limit a client can request
    max_limit = 30

    # Override the offset query parameter name
    offset_query_param = "start"

    # Override the limit query parameter name
    limit_query_param = "items"


class SelectPagination(LimitOffsetPagination):
    # Set the default limit
    default_limit = 20  # Default number of items per page

    # Set the maximum limit a client can request
    max_limit = 30

    # Override the offset query parameter name
    offset_query_param = "start"

    # Override the limit query parameter name
    limit_query_param = "items"
