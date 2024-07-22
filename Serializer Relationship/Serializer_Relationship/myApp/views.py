from django.shortcuts import render
from .models import Singer,Songs
from .serializers import SingerSerializer,SongsSerializer
from rest_framework import viewsets
# Create your views here.

class SongsView(viewsets.ModelViewSet):
    queryset=Songs.objects.all()
    serializer_class=SongsSerializer
    
    
class SingerView(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer
