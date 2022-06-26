from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IntroViewSet, TafseerViewSet

router = DefaultRouter()
router.register('list', TafseerViewSet, basename='tafseer')
router.register('intro', IntroViewSet, basename='intro')

urlpatterns = [
    path('', include(router.urls)),
]
