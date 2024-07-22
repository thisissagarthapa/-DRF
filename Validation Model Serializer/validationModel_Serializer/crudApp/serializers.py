from rest_framework import serializers
from .models import Student



# custom validation
def validators_r(value):
    if value[0].lower()!="r":
        raise serializers.ValidationError('value must start with R')
    return value

class StudentSerializer(serializers.ModelSerializer):
    name=serializers.CharField(validators=[validators_r])
    class Meta:
        model=Student
        fields=['id','name','age','email']
        
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

