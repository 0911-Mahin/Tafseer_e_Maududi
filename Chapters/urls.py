from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'', views.ChapterViewSet, basename='chapter')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), name='authen'),
]
