# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hikaye', '0003_auto_20150819_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
