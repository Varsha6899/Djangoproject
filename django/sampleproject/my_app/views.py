from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from .models import my_app
from .serializers import Serializer

class my_appView(viewsets.ModelViewSet):
   queryset = my_app.objects.all()
   serializer_class = Serializer