from django.db import models


class Rub(models.Model):
    rub_number = models.IntegerField()
    verse_count = models.IntegerField()
