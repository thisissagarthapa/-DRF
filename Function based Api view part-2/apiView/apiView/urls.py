
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/',views.studentinfo),
    path('stuinfo/<int:id>/',views.studentinfo),
]
