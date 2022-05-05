from django.urls import reverse
from rest_framework import serializers
from .models import Juz


class JuzSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='juz-detail', lookup_field='juz_number')
    verses = serializers.SerializerMethodField('get_verses_link')

    def get_verses_link(self, juz):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('verse-by-juz', kwargs={'juz_number': juz.juz_number}))

    class Meta:
        model = Juz
        fields = ['detail', 'id', 'juz_number', 'verse_count', 'verses']
