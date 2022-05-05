from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import VerseViewSet

router = DefaultRouter()
router.register('', VerseViewSet, basename='verse')

i = 0
while i < len(router.urls):
    if router.urls[i].name == 'verse-by-chapter':
        router.urls.remove(router.urls[i])
        i -= 1
    i += 1

urlpatterns = [
    path('', include(router.urls)),
    path('by_chapter/<int:chapter_number>/',
         VerseViewSet.as_view({'get': 'by_chapter'}), name='verse-by-chapter')
]
