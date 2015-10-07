from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User_id (models.Model):
    user_id=models.self

    MALE= 'm'
    FEMALE='f'
    OTHER='O'

    GENDER_CHOICES =(
    (MALE,'male'),
    (FEMALE, 'female')
    (OTHER,'Other')
)

    gender=models.CharField(max_length=1, choices= ())

    def__str__(self):
        return self.user_id()


class Movie(models.Model):
    movie_id=models.CharField(max_length=50)



    def__str__(self):
        return self.movie_id


class Rating(models.Model):
    user_id = models.ForeignKey(User_id)
    movie = models.ForeignKey(Movie)
    rating = models.PositiveSmallIntegerField()

    def__str__(self):
        return 'user {} gives {} a {}'.format(self.user, self.movie, self.rating)
