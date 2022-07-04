from django.urls import include, path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('levels', views.GlucoseLevelView, basename='levels')

urlpatterns = [
    path('', include(router.urls))
]
