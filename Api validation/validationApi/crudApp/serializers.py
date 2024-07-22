from rest_framework import serializers
from .models import Student



# custom validation
def validators_r(value):
    if value[0].lower()!="r":
        raise serializers.ValidationError('value must start with R')
    return value

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100,validators=[validators_r])
    age=serializers.IntegerField()
    email=serializers.EmailField()
       
       
       
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.age=validated_data.get('age',instance.age)
        instance.email=validated_data.get('email',instance.email)
        instance.save()
        return instance
    
    # Field level validation
    def validate_age(self,value):

        if value>=30:
            raise serializers.ValidationError('age must be less than 30')
        return value
    
    # object level validation
    def validate(self,data):
        if  data['name']=="saurav":
            raise serializers.ValidationError('This name cannot be used')
        return data
    
