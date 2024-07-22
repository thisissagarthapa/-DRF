
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/',views.StudentApi.as_view()),
    path('stuinfo/<int:id>/',views.StudentApi.as_view()),
]
