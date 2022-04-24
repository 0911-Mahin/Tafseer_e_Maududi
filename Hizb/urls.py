from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import HizbViewSet

router = DefaultRouter()
router.register('', HizbViewSet, basename='hizb')

urlpatterns = [
    path('', include(router.urls))
]
