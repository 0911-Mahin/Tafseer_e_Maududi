from django.urls import reverse
from rest_framework import serializers

from .models import Rub


class RubSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='rub-detail', lookup_field='rub_number')
    verses = serializers.SerializerMethodField('get_verses_link')

    def get_verses_link(self, rub):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('verse-by-rub', kwargs={'rub_number': rub.rub_number}))

    class Meta:
        model = Rub
        fields = ['detail', 'id', 'rub_number', 'verse_count', 'verses']
