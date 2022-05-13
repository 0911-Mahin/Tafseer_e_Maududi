from django.db import models

from Verse.models import Verse


class Ayah(models.Model):
    sentence = models.FileField()
    verse = models.ForeignKey(
        Verse, on_delete=models.CASCADE, related_name='ayah')
