from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class StudentViewsets(viewsets.ViewSet):
    def list(self,request):
        stu=Student.objects.all()
        serializer=StudentSerializers(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def retrieve(self,request,pk=None):
        if id is not None:
            stu=Student.objects.get(id=pk)
            serializer=StudentSerializers(stu)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
    def create(self,request):
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        stu=Student.objects.get(id=pk)
        serializer=StudentSerializers(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated completely'},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        stu=Student.objects.get(id=pk)
        serializer=StudentSerializers(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated partially'},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        stu=Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg':'data deleted'})