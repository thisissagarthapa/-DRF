from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentModelviewSets(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    

# class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializers