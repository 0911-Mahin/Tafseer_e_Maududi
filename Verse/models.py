from django.db import models

from Chapters.models import Chapter
from Juz.models import Juz
from Hizb.models import Hizb
from Rub.models import Rub


class Verse(models.Model):
    verse_number = models.IntegerField()
    verse_key = models.CharField(max_length=8)
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, related_name='verses')
    juz = models.ForeignKey(
        Juz, on_delete=models.CASCADE, related_name='verses')
    hizb = models.ForeignKey(
        Hizb, on_delete=models.CASCADE, related_name='verses')
    rub = models.ForeignKey(
        Rub, on_delete=models.CASCADE, related_name='verses')
    recitation = models.FileField()
    translation = models.CharField(max_length=100000)
    ayah = models.CharField(max_length=200)
