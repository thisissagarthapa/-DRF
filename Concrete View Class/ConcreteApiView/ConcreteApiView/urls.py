
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/',views.StudentListCreateAPIView.as_view()),
    path('stuinfo/<int:pk>/',views.StudentRetrieveUpdateDestroyAPIView.as_view()),
]
