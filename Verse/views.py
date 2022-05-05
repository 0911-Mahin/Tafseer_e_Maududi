from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Chapters.models import Chapter
from .models import Verse
from .serializers import VerseSerializer


class VerseViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'verse_number'
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer

    @action(detail=True, methods=['get'])
    def by_chapter(self, request, chapter_number):
        chapter = Chapter.objects.get(pk=chapter_number)
        page = self.paginate_queryset(chapter.verses.all())
        serializer = VerseSerializer(
            page, many=True, context={'request': request})
        return Response(serializer.data)
