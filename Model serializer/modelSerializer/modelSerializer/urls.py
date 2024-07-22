
from django.contrib import admin
from django.urls import path
from crudApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stuinfo/',views.student_info)#FUNCTION BASED URLS 
    path('stuinfo/',views.StudentAPI.as_view())
]
