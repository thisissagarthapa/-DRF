from django.urls import path
from .views import *
urlpatterns = [
    path('stuinfo/',StudentAPI.as_view())
]
