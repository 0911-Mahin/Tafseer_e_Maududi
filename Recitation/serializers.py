from django.urls import reverse
from rest_framework import serializers

from .models import Recitation


class RecitationSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='recitation-detail', lookup_field='id')
    audio = serializers.SerializerMethodField('get_audio_url')
    verse = serializers.SerializerMethodField('get_verse')

    def get_audio_url(self, recitation):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('recitation-audio', kwargs={'id': recitation.id}))

    def get_verse(self, recitation):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('verse-detail', kwargs={'verse_number': recitation.verse.verse_number}))

    class Meta:
        model = Recitation
        fields = ['detail', 'id', 'audio', 'verse']
