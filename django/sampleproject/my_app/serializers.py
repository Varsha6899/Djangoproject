from rest_framework import serializers
from .models import my_app

class Serializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = my_app
       fields = ('id', 'real_name', 'tz', 'activity_periods')