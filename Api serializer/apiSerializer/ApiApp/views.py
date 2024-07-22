from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
# Create your views here.
def Student_info(request):
    stu=Student.objects.all()
    print(stu)
    serializer=StudentSerializer(stu,many=True)
    print(serializer)
    return JsonResponse(serializer.data,safe=False)
