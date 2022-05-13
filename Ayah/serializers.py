from django.urls import reverse
from rest_framework import serializers
from .models import Ayah


class AyahSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='ayah-detail', lookup_field='id')
    verse = serializers.SerializerMethodField('get_verses_link')
    sentence = serializers.SerializerMethodField('get_sentence')

    def get_verses_link(self, ayah):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('verse-detail', kwargs={'verse_number': ayah.verse.id}))

    def get_sentence(self, ayah):
        return ayah.sentence.open().read()[:-4]

    class Meta:
        model = Ayah
        fields = ['detail', 'id', 'sentence', 'verse']
