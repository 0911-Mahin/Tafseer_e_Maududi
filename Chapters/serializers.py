from rest_framework import serializers
from .models import Chapter


class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chapter
        feilds = ['url', 'surah_number', 'name', 'verses',
                  'revelation_place', 'revelation_order', 'translated_name']
