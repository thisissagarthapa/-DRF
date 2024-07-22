from rest_framework.pagination import LimitOffsetPagination, CursorPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5

class MyCursorPagination(CursorPagination):
    page_size = 5
