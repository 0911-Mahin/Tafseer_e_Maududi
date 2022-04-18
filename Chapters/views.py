from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiResponse
from drf_spectacular.types import OpenApiTypes
from rest_framework import viewsets

from .serializers import ChapterSerializer
from .models import Chapter

# Create your views here.


class ChapterViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'surah_number'
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(name='page', description='Page Number of chapters according to 10/page Pagination',
                             required=False, type=int, location=OpenApiParameter.QUERY,
                             examples=[
                                 OpenApiExample('Page 1', summary='First 10 results',
                                                description='To Get First 10 chapters out of all', value=1),
                                 OpenApiExample('Page 2', summary='From results 10 to 20',
                                                description='To Get from chapter 10 to 20 out of all', value=2)
                             ])
        ], description='Get list of all Chapters in Quran (Consider Pagination)',
        responses={
            '200': ChapterSerializer,
            '401': OpenApiResponse(response=401, description='Unauthorized. Authorization Credentials not Provided'),
            '404': OpenApiResponse(response=404, description='Page Not Found'),
            '429': OpenApiResponse(response=429, description='Throttled. Rate limit exceeded')
        })
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        parameters=[
            OpenApiParameter(name='surah_number', description='Number of Surah to get details of',
                             required=False, type=int, location=OpenApiParameter.PATH,
                             examples=[
                                 OpenApiExample('Surah 1', summary='First Surah',
                                                description='To Get details of first Surah in Quran', value=1),
                                 OpenApiExample('Surah 2', summary='Second Surah',
                                                description='To Get details of second Surah in Quran', value=2)
                             ])
        ], description='Retrive a chapter of Quran',
        responses={
            '200': ChapterSerializer,
            '401': OpenApiResponse(response=401, description='Unauthorized. Authorization Credentials not Provided'),
            '404': OpenApiResponse(response=404, description='Surah Not Found'),
            '429': OpenApiResponse(response=429, description='Throttled. Rate limit exceeded')
        })
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
