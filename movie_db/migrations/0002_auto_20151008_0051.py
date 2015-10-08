# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie_db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_id',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='user_id',
            name='age',
            field=models.PositiveIntegerField(default=datetime.datetime(2015, 10, 8, 0, 50, 41, 975879, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_id',
            name='zipcode',
            field=models.CharField(max_length=5, default=datetime.datetime(2015, 10, 8, 0, 51, 41, 111706, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_id',
            name='gender',
            field=models.CharField(max_length=1, choices=[('m', 'male'), ('f', 'female'), ('O', 'other'), ('Did not answer', 'Did not answer')]),
        ),
    ]
