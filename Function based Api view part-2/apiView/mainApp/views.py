from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def studentinfo(request,id=None):
    if request.method=='GET': 
        if id is not None:
            stu=Student.objects.get(id=id)
            serializers=StudentSerializers(stu)
            return Response({'data':serializers.data})
        stu=Student.objects.all()
        serializers=StudentSerializers(stu,many=True)
        return Response(serializers.data)

    
    if request.method=='POST':
        serializers=StudentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'data created'})
        return Response(serializers.errors)
    
    if request.method=='PUT':
        stu=Student.objects.get(id=id)
        serializers=StudentSerializers(stu,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'data updated'})
        return Response({'msg':'invalid error'})
 
    if request.method=='DELETE':
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'delete'})
