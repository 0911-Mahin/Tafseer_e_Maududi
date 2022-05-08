from rest_framework import viewsets

from .models import Translation
from .serializers import TranslationSerializer


class TranslationViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'id'
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
