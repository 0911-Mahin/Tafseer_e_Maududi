from django.http import FileResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from Chapters.models import Chapter
from Juz.models import Juz
from Hizb.models import Hizb
from Rub.models import Rub
from .models import Verse
from .serializers import VerseSerializer


class VerseViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'verse_number'
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer

    @action(detail=True, methods=['get'])
    def recitation(self, request, verse_number):
        verse = self.get_object()
        return FileResponse(verse.recitation.open())

    @action(detail=False, methods=['get'], url_path=r'by_chapter/(?P<chapter_number>\d+)')
    def by_chapter(self, request, chapter_number):
        try:
            chapter = Chapter.objects.get(pk=chapter_number)
            page = self.paginate_queryset(chapter.verses.all())
            serializer = VerseSerializer(
                page, many=True, context={'request': request})
            return Response(serializer.data)
        except Chapter.DoesNotExist:
            return Response({'detail', 'Not Found.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'], url_path=r'by_juz/(?P<juz_number>\d+)')
    def by_juz(self, request, juz_number):
        try:
            juz = Juz.objects.get(pk=juz_number)
            page = self.paginate_queryset(juz.verses.all())
            serializer = VerseSerializer(
                page, many=True, context={'request': request})
            return Response(serializer.data)
        except Juz.DoesNotExist:
            return Response({'detail': 'Not Found.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'], url_path=r'by_hizb/(?P<hizb_number>\d+)')
    def by_hizb(self, request, hizb_number):
        try:
            hizb = Hizb.objects.get(pk=hizb_number)
            page = self.paginate_queryset(hizb.verses.all())
            serializer = VerseSerializer(
                page, many=True, context={'request': request})
            return Response(serializer.data)
        except Hizb.DoesNotExist:
            return Response({'detail': 'Not Found.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'], url_path=r'by_rub/(?P<rub_number>\d+)')
    def by_rub(self, request, rub_number):
        try:
            rub = Rub.objects.get(pk=rub_number)
            page = self.paginate_queryset(rub.verses.all())
            serializer = VerseSerializer(
                page, many=True, context={'request': request})
            return Response(serializer.data)
        except Rub.DoesNotExist:
            return Response({'detail': 'Not Found.'}, status=status.HTTP_404_NOT_FOUND)
