from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TafseerViewSet

router = DefaultRouter()
router.register('', TafseerViewSet, basename='tafseer')

urlpatterns = [
    path('', include(router.urls)),
]
