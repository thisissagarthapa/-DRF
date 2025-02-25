from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    age=serializers.IntegerField()
    email=serializers.EmailField()
    
    
    def create(self,validate_data):
        return Student.objects.create(**validate_data)