# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('hikaye', '0002_auto_20150819_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='children',
        ),
        migrations.RemoveField(
            model_name='story',
            name='release_date',
        ),
        migrations.AddField(
            model_name='story',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 19, 17, 7, 27, 248690, tzinfo=utc), auto_created=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='is_reported',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='story',
            name='parent',
            field=models.ForeignKey(blank=True, to='hikaye.Story', null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='score',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='story',
            name='writer',
            field=models.ForeignKey(related_name='stories', to=settings.AUTH_USER_MODEL),
        ),
    ]
