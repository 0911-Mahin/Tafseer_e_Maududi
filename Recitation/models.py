from django.db import models

from Verse.models import Verse


class Recitation(models.Model):
    audio = models.FileField()
    verse = models.ForeignKey(
        Verse, on_delete=models.CASCADE, related_name='recitation')
