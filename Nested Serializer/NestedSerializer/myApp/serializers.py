from .models import Singer,Songs
from rest_framework import serializers

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Songs
        fields='__all__'
        
class SingerSerializer(serializers.ModelSerializer):
    song=SongsSerializer(many=True,read_only=True)
    class Meta:
        model=Singer
        fields='__all__'
        
