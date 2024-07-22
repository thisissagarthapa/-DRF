from django.contrib import admin
from .models import Singer,Songs
# Register your models here.

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display=['id','name','gender']
    
@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display=['id','title','singer','duration']