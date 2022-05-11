from django.urls import include, path
from rest_framework.routers import DefaultRouter

from.views import RecitationViewSet

router = DefaultRouter()
router.register('', RecitationViewSet, 'recitation')

urlpatterns = [
    path('', include(router.urls))
]
