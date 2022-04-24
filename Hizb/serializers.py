from rest_framework import serializers

from .models import Hizb


class HizbSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='hizb-detail', lookup_field='hizb_number')

    class Meta:
        model = Hizb
        fields = ['detail', 'id', 'hizb_number', 'verse_count']
