from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from Chapters.models import Chapter
from Juz.models import Juz
from .models import Verse
from .serializers import VerseSerializer


class VerseViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'verse_number'
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer

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
