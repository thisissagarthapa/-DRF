from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter,
# Create your views here.



# through the default  settings  of django backend filter
""" class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filterset_fields=['passBy'] """
    
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[SearchFilter]
    search_fields=['^name']  #starts with 
    