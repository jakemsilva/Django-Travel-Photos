# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='picture_big',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='picture_small',
        ),
    ]
