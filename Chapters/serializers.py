from django.urls import reverse
from rest_framework import serializers
from .models import Chapter


class ChapterSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='chapter-detail', lookup_field='surah_number')
    verses = serializers.SerializerMethodField('get_verses_link')
    tafseers = serializers.SerializerMethodField('get_tafseers_link')

    def get_verses_link(self, chapter):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('verse-by-chapter', kwargs={'chapter_number': chapter.surah_number}))

    def get_tafseers_link(self, chapter):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('tafseer-by-chapter', kwargs={'chapter_number': chapter.surah_number}))

    class Meta:
        model = Chapter
        fields = ['detail', 'id', 'surah_number', 'name', 'verse_count', 'verses', 'tafseers',
                  'revelation_place', 'revelation_order', 'translated_name', 'Intro']
