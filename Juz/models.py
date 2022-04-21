from django.db import models


class Juz(models.Model):
    juz_number = models.IntegerField()
    verse_count = models.IntegerField()
