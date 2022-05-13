from django.http import FileResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Recitation
from .serializers import RecitationSerializer


class RecitationViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'id'
    queryset = Recitation.objects.all()
    serializer_class = RecitationSerializer

    @action(detail=True, methods=['get'])
    def audio(self, request, id):
        recitation = self.get_object()
        return FileResponse(recitation.audio.open())
