from django.contrib import admin

# Register your models here.
from .models import my_app
admin.site.register(my_app)
