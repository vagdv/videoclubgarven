from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    urlTrailer = models.CharField(max_length=100)
    desc = models.CharField(max_length=400)
    year = models.DateField()
    director = models.CharField(max_length=100)
    cast = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    rating = models.IntegerField

    def __str__(self):
        return self.name + '\n'
