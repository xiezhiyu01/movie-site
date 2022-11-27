from django.db import models

# Create your models here.
from django.db import models


# class CelebrityCoop(models.Model):
#     name = models.CharField(max_length=200)
#     imgSrc = models.CharField(max_length=200)
#     count = models.IntegerField()


class Celebrity(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=300)
    intro = models.CharField(max_length=1000)
    imgSrc = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    movies = models.CharField(max_length=1000)



class Movie(models.Model):
    id = models.IntegerField
    title = models.CharField(max_length=200)
    rating = models.FloatField(max_length=10)
    summary = models.CharField(max_length=1000)
    imgSrc = models.CharField(max_length=200)
    comment1 = models.CharField(max_length=1000)
    comment2 = models.CharField(max_length=1000)
    comment3 = models.CharField(max_length=1000)
    comment4 = models.CharField(max_length=1000)
    comment5 = models.CharField(max_length=1000)
    actors = models.CharField(max_length=1000)

