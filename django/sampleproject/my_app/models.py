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