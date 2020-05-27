from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('my_app', views.my_appView)

urlpatterns = [
  path('', include(router.urls))
]