from rest_framework.routers import DefaultRouter
from django.urls import include, path

from Juz.views import JuzViewSet

router = DefaultRouter()
router.register('', JuzViewSet, 'juz')

urlpatterns = [
    path('', include(router.urls))
]
