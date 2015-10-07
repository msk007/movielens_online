from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User_id (models.Model):
    user_id=models


class Movie(models.Model):
    movie_id=models.CharField(max_length=200)

class Rating(models.Model):
    user_id = models.ForeignKey(User_id)
    movie = models.ForeignKey(Movie)
    rating = models.FloatField()

    def__str__(self):
