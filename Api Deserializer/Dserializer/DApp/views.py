from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

import io
# Create your views here.
@csrf_exempt
def Student_create(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        Serializer=StudentSerializers(data=python_data)
        if Serializer.is_valid():
            Serializer.save()
            res={'msg':'student created sucessfully'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
    
        json_data=JSONRenderer().render(Serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

        