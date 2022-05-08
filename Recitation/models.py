from django.db import models

from Verse.models import Verse


class Recitation(models.Model):
    recitation = models.CharField(max_length=32)
    verse = models.ForeignKey(
        Verse, on_delete=models.CASCADE, related_name='recitation')
