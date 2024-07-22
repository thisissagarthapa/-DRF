from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
from mainApp.pagination import MyLimitOffsetPagination, MyCursorPagination

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyLimitOffsetPagination  # Use MyLimitOffsetPagination
    # pagination_class = MyCursorPagination  # Use MyCursorPagination if needed
