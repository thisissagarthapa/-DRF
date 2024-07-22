from .models import Singer,Songs
from rest_framework import serializers

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Songs
        fields='__all__'
        
class SingerSerializer(serializers.ModelSerializer):
    # song=serializers.StringRelatedField(many=True,read_only=True)
    # song=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # song=serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')
    class Meta:
        model=Singer
        fields='__all__'
        
