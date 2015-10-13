from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class User_id (models.Model):
    user_id=models.CharField(max_length=10)

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
    zipcode = models.CharField(max_length=5, null=True)
    age = models.PositiveIntegerField=56
    occupation= models.CharField(max_length=40, null=True)

    def __str__(self):
        return str(self.id)


class Movie(models.Model):
    movie_id=models.CharField(max_length=50)

    def average_ratings(self):
        return self. rating_set.aggregate(models.Avg('stars'))['stars__avg']

    def __str__(self):
        return self.movie_id


class Rating(models.Model):
    user_id = models.ForeignKey(User_id)
    movie = models.ForeignKey(Movie)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return 'user {} gives {} a {}'.format(self.user, self.movie, self.rating)



def load_ml_data():
    import csv
    import json
    import re

    users=[]

    with open('ml-1m/users.dat', encoding='Windows-1252') as f:


        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames ='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
                                delimiter='\t')

        for row in reader:
            
            ['fields']:{
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation':row['Occupation'],
                    'zipcode': row['Zip-code']
                },
                'model': 'movie_db.Rating',
                'pk': int(row['User_id']),
            }


            users.append(user)

        with open('users.json', 'w') as f:
            f.write(json.dump(users))

        print(json.dumps(users, sort_keys=True, indent=4, separators=(',', ': ')))


    def Import_all_data():

        import_all_data
