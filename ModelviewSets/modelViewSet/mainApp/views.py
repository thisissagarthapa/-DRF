from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet

# class StudentModelviewSets(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializers
    
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers