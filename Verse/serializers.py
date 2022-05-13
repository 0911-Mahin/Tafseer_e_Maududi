from django.urls import reverse
from rest_framework import serializers

from .models import Verse


class VerseSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='verse-detail', lookup_field='verse_number')
    chapter = serializers.SerializerMethodField('get_chapter')
    juz = serializers.SerializerMethodField('get_juz')
    hizb = serializers.SerializerMethodField('get_hizb')
    rub = serializers.SerializerMethodField('get_rub')
    recitation = serializers.SerializerMethodField('get_recitation')

    def get_chapter(self, verse):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('chapter-detail', kwargs={'surah_number': verse.chapter.id}))

    def get_juz(self, verse):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('juz-detail', kwargs={'juz_number': verse.juz.id}))

    def get_hizb(self, verse):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('hizb-detail', kwargs={'hizb_number': verse.hizb.id}))

    def get_rub(self, verse):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('rub-detail', kwargs={'rub_number': verse.rub.id}))

    def get_recitation(self, verse):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('recitation-detail', kwargs={'id': verse.recitation.get().id}))

    class Meta:
        model = Verse
        fields = ['detail', 'id', 'verse_number',
                  'verse_key', 'chapter', 'juz', 'hizb', 'rub', 'recitation']
