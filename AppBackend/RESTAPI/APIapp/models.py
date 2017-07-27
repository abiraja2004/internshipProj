from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Logo(models.Model):
    company = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Map(models.Model):
    name = models.CharField(max_length=100)
    mapFilePath = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class MapHasLogo(models.Model):
    logoID = models.ForeignKey(Logo, on_delete=models.CASCADE)
    mapID = models.ForeignKey(Map, on_delete=models.CASCADE)


class MapHasTags(models.Model):
    mapID = models.ForeignKey(Map, on_delete=models.CASCADE)
    TagID = models.ForeignKey(Tag, on_delete=models.CASCADE)











