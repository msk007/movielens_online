from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User_id (models.Model):
    user=models.CharField(max_length=10)

    MALE= 'm'
    FEMALE='f'
    OTHER='O'
    X='Did not answer'

    GENDER_CHOICES =(
    (MALE,'male'),
    (FEMALE, 'female'),
    (OTHER,'other'),
    (X, 'Did not answer'),
)

    gender=models.CharField(max_length=1, choices= GENDER_CHOICES)
    zipcode = models.CharField(max_length=5)
    age = models.PositiveIntegerField()

    #def__str__(self):
        #return self.user_id()


class Movie(models.Model):
    movie_id=models.CharField(max_length=50)



    #def__str__(self):
        #return self.movie_id


class Rating(models.Model):
    user_id = models.ForeignKey(User_id)
    movie = models.ForeignKey(Movie)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return 'user {} gives {} a {}'.format(self.user, self.movie, self.rating)

    users=[]

    def load_ml_data():
        import csv
        import json

        with open('ml-1m/movies.dat', encoding='Windows-1252') as f:
            reader = csv.DictReader(f,
                                fieldnames= 'UserID::Gender::Age::Occupation::Zip-code'.split('::'),
                                delimiter='::')

            for row in reader:
                user= {}
