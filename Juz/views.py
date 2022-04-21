from rest_framework import viewsets

from .models import Juz
from .serializers import JuzSerializer


class JuzViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'juz_number'
    queryset = Juz.objects.all()
    serializer_class = JuzSerializer
