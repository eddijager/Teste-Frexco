
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'region', views.RegionViewSet)
router.register(r'fruit', views.FruitViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]