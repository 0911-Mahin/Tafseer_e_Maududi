from django.urls import reverse
from rest_framework import serializers

from .models import Tafseer, Intro


class TafseerSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='tafseer-detail')
    chapter = serializers.SerializerMethodField('get_chapter')
    verses = serializers.SerializerMethodField('get_verses')
    intro = serializers.SerializerMethodField('get_intro')

    def get_chapter(self, tafseer):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('chapter-detail', kwargs={'surah_number': tafseer.verses.first().chapter.id}))

    def get_verses(self, tafseer):
        request = self.context.get('request')
        uris = []
        for verse in tafseer.verses.all():
            uris.append(request.build_absolute_uri(
                reverse('verse-detail', kwargs={'verse_number': verse.verse_number})))
        return uris

    def get_intro(self, tafseer):
        request = self.context.get('request')
        return request.build_absolute_uri(
            reverse('intro-detail', kwargs={'pk': tafseer.intro.all().first().id}))

    class Meta:
        model = Tafseer
        fields = ['detail', 'chapter', 'id', 'text', 'verses', 'intro']


class IntroSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='intro-detail')
    tafseers = serializers.SerializerMethodField('get_tafseers')

    def get_tafseers(self, intro):
        request = self.context.get('request')
        uris = []
        for tafseer in intro.tafseers.all():
            uris.append(request.build_absolute_uri(
                reverse('tafseer-detail', kwargs={'pk': tafseer.id})))
        return uris

    class Meta:
        model = Intro
        fields = ['detail', 'id', 'text', 'tafseers']
