# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('movie', models.ForeignKey(to='movie_db.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='User_id',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='user_id',
            field=models.ForeignKey(to='movie_db.User_id'),
        ),
    ]
