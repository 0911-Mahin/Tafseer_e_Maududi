from django.urls import reverse
from rest_framework import serializers

from .models import Hizb


class HizbSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='hizb-detail', lookup_field='hizb_number')
    verses = serializers.SerializerMethodField('get_verses_link')

    def get_verses_link(self, hizb):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('verse-by-hizb', kwargs={'hizb_number': hizb.hizb_number}))

    class Meta:
        model = Hizb
        fields = ['detail', 'id', 'hizb_number', 'verse_count', 'verses']
