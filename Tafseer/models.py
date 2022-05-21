from django.db import models

from Verse.models import Verse


class Tafseer(models.Model):
    text = models.CharField(max_length=1000)
    verses = models.ManyToManyField(Verse, related_name='tafseer')
