from rest_framework import serializers
from .models import Juz


class JuzSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='juz-detail', lookup_field='juz_number')

    class Meta:
        model = Juz
        fields = ['detail', 'id', 'juz_number', 'verse_count']
