from django.db import models

from Verse.models import Verse


class Translation(models.Model):
    translation = models.CharField(max_length=32)
    verse = models.ForeignKey(
        Verse, on_delete=models.CASCADE, related_name='translation')
