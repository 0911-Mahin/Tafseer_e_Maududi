from rest_framework import serializers
from .models import Chapter


class ChapterSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='chapter-detail', lookup_field='surah_number')

    class Meta:
        model = Chapter
        fields = ['detail', 'id', 'surah_number', 'name', 'verses',
                  'revelation_place', 'revelation_order', 'translated_name']
