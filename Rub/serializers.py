from rest_framework import serializers

from .models import Rub


class RubSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='rub-detail', lookup_field='rub_number')

    class Meta:
        model = Rub
        fields = ['detail', 'id', 'rub_number', 'verse_count']
