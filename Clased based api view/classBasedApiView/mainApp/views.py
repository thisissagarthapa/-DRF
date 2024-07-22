from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class StudentApi(APIView):
    def get(self,request,id=None,format=None):
            if id is not None:
                stu=Student.objects.get(id=id)
                serializers=StudentSerializers(stu)
                return Response({'data':serializers.data})
            stu=Student.objects.all()
            serializers=StudentSerializers(stu,many=True)
            return Response(serializers.data)

    def post(self,request,format=None):
        serializers=StudentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'data created'})
        return Response(serializers.errors)
    
    def put(self,request,id=None,format=None):
        stu=Student.objects.get(id=id)
        serializers=StudentSerializers(stu,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'data updated'})
        return Response({'msg':'invalid error'})
    
    def patch(self,request,id=None,format=None):
        stu=Student.objects.get(id=id)
        serializers=StudentSerializers(stu,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'partial data updated'})
        return Response({'msg':'invalid error'})
 
    def delete(self,request,id=None,format=None):
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'delete'})
