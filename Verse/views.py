from rest_framework import viewsets

from .models import Verse
from .serializers import VerseSerializer


class VerseViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'verse_number'
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer
