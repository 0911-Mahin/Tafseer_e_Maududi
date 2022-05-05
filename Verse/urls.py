from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import VerseViewSet

router = DefaultRouter()
router.register('', VerseViewSet, basename='verse')

urlpatterns = [
    path('', include(router.urls)),
]
