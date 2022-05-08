from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TranslationViewSet

router = DefaultRouter()
router.register('', TranslationViewSet, 'translation')

urlpatterns = [
    path('', include(router.urls)),
]
