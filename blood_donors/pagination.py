from rest_framework.pagination import CursorPagination


class BloodDonorPagination(CursorPagination):
    page_size = 20
    ordering = "id"
