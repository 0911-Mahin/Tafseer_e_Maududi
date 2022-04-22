from django.shortcuts import render
from rest_framework import viewsets

from .models import Hizb
from .serializers import HizbSerializer


class HizbViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'hizb_number'
    queryset = Hizb.objects.all()
    serializer_class = HizbSerializer
