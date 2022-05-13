from rest_framework import viewsets

from .models import Ayah
from .serializers import AyahSerializer


class AyahViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'id'
    queryset = Ayah.objects.all()
    serializer_class = AyahSerializer
