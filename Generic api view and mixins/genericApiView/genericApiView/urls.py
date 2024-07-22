
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/',views.ListModelView.as_view()),
    path('stuinfo/<int:pk>/',views.RetrieveModelView.as_view()),
    # path('stuinfo/',views.CreateModelView.as_view()),
    # path('stuinfo/<int:pk>/',views.UpdateModelView.as_view()),
    # path('stuinfo/<int:pk>/',views.DestroyModelView.as_view()),
]
