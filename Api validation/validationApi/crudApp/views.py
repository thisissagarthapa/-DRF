import io

from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from django.views import View
from rest_framework.views import APIView
from django.utils.decorators import method_decorator

# CLASS BASED VIEW
@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
    def get(self,request):
        if request.method=="GET":
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            id=python_data.get("id",None)
            if id is not None:
                stu=Student.objects.get(id=id)
                serializer=StudentSerializer(stu)
                return JsonResponse(serializer.data)
            stu=Student.objects.all()
            serializer=StudentSerializer(stu,many=True)
            return JsonResponse(serializer.data,safe=False)
        
    def post(self,request,*args, **kwargs):
        if request.method=="POST":
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            serializer=StudentSerializer(data=python_data)
            if serializer.is_valid():
                serializer.save()
                res={'msg':'data created successfully'}
                return JsonResponse(res)
            return JsonResponse(serializer.errors)
        
    def put(self,request,*args, **kwargs):
        if request.method=="PUT":
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            id=python_data.get('id')
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu,data=python_data)
            # serializer=StudentSerializer(stu,data=python_data,partial=True) #For partial update
            if serializer.is_valid():
                serializer.save()
                res={'msg':'data updated'}
                return JsonResponse(res)
            
            return JsonResponse(serializer.errors)
    
    def delete(self,request,*args, **kwargs): 
        if request.method=="DELETE":
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            id=python_data.get('id')
            stu=Student.objects.get(id=id)
            stu.delete()
            res={
                'msg':'data deleted'
            }
            return JsonResponse(res,safe=False)

        