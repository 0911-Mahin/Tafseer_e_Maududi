from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from Chapters.models import Chapter
from .models import Tafseer, Intro
from .serializers import TafseerSerializer, IntroSerializer


class TafseerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tafseer.objects.all()
    serializer_class = TafseerSerializer

    @action(detail=False, methods=['get'], url_path=r'by_chapter/(?P<chapter_number>\d+)')
    def by_chapter(self, request, chapter_number):
        try:
            chapter = Chapter.objects.get(pk=chapter_number)
            tafseers = Tafseer.objects.filter(
                verses__in=chapter.verses.all()).distinct()
            page = self.paginate_queryset(tafseers)
            serializer = TafseerSerializer(
                page, many=True, context={'request': request})
            return Response(serializer.data)
        except Chapter.DoesNotExist:
            return Response({'detail', 'Not Found.'}, status=status.HTTP_404_NOT_FOUND)


class IntroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Intro.objects.all()
    serializer_class = IntroSerializer

    @action(detail=False, methods=['get'], url_path=r'by_chapter/(?P<chapter_number>\d+)')
    def by_chapter(self, request, chapter_number):
        try:
            intro = Intro.objects.get(pk=chapter_number)
            serializer = IntroSerializer(intro, context={'request': request})
            return Response(serializer.data)
        except Chapter.DoesNotExist:
            return Response({'detail', 'Not Found.'}, status=status.HTTP_404_NOT_FOUND)
