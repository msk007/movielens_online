# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_id',
            name='occupation',
            field=models.CharField(null=True, max_length=40),
        ),
        migrations.AddField(
            model_name='user_id',
            name='zipcode',
            field=models.CharField(null=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='user_id',
            name='gender',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female'), ('O', 'other'), ('Did not answer', 'Did not answer')], max_length=1),
        ),
    ]
