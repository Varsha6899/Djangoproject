# Djangoproject

## Steps for creating django rest API

##Install DJango RestFramework / prerequisites
#pip install django
#pip install djangorestframework

##Create django app
django-admin startapp my_app

##Modify your django application settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'my_app',
]

##Implement DJango RestFramework
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),
]

##Create a model for employee_api on my_app/models.py  
from django.db import models

# Create your models here.

class my_app(models.Model):
    ok = 'true'
    id = models.IntegerField
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=50)
    activity_periods = models.CharField(max_length=50)
    def __str__(self):
        return self.id
        
 #Add your model into admin console
 from django.contrib import admin
 
# Register your models here.
from .models import my_app
admin.site.register(my_app)

## Create Serializers on my_app/serializers.py
from rest_framework import serializers
from .models import my_app

class Serializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = my_app
       fields = ('id', 'real_name', 'tz', 'activity_periods')
       
       
## Update views as per the serializers on departments/views.py
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import my_app
from .serializers import Serializer

class my_appView(viewsets.ModelViewSet):
   queryset = my_app.objects.all()
   serializer_class = Serializer


## API URLs using automatic URL routing. on my_app/urls.py
from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('my_app', views.my_appView)

urlpatterns = [
  path('', include(router.urls))
]





        
        
        
        
