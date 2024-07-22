
from django.contrib import admin
from django.urls import path,include
from mainApp import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register('stuinfo',views.StudentViewsets,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
