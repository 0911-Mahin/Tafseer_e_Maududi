from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AyahViewSet

router = DefaultRouter()
router.register('', AyahViewSet, 'ayah')

urlpatterns = [
    path('', include(router.urls))
]
