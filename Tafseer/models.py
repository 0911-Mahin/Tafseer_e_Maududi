from django.db import models

from Verse.models import Verse


class Tafseer(models.Model):
    text = models.FileField()
    verses = models.ManyToManyField(Verse, related_name='tafseer')


class Intro(models.Model):
    text = models.FileField()
    tafseers = models.ManyToManyField(Tafseer, related_name='intro')
