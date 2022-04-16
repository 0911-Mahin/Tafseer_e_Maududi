from django.db import models

# Create your models here.


class Chapter(models.Model):
    surah_number = models.IntegerField()
    name = models.CharField(max_length=32)
    verses = models.IntegerField()
    revelation_place = models.CharField(max_length=16)
    revelation_order = models.IntegerField()
    translated_name = models.CharField(max_length=64)

    def __str__(self):
        return f'Surah {self.name}({self.translated_name}) was revealed in {self.revelation_place} with {self.verses} verses'
