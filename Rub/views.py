from rest_framework import viewsets

from .models import Rub
from .serializers import RubSerializer


class RubViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'rub_number'
    queryset = Rub.objects.all()
    serializer_class = RubSerializer
