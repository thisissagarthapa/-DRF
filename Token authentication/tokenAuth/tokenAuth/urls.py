
from django.contrib import admin
from django.urls import path,include
from mainApp import views
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
from mainApp.auth import CustomAuthToken
router=DefaultRouter()

router.register('stuinfo',views.StudentModelviewSets,basename='student')
# router.register('stuinfo',views.StudentReadOnlyModelViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('gettoken/',CustomAuthToken.as_view())
    # path('gettoken/',obtain_auth_token)
]
















