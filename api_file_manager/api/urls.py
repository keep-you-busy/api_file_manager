from django.urls import path, include
from rest_framework import routers

from api.views import FileViewSet


router_v1 = routers.DefaultRouter()

router_v1.register('files', FileViewSet, basename='files')
urlpatterns = [
    path('', include(router_v1.urls)),
]
