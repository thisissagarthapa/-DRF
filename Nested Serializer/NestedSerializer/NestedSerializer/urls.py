
from django.contrib import admin
from django.urls import path,include
from myApp import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register('Songs/',views.SongsView,basename='songs')
router.register('Singer/',views.SingerView,basename='singer')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
