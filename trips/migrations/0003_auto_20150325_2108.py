# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import trips.models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_auto_20150325_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='picture_big',
            field=imagekit.models.fields.ProcessedImageField(upload_to=trips.models.get_upload_path_big, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='picture_small',
            field=imagekit.models.fields.ProcessedImageField(upload_to=trips.models.get_upload_path_small, blank=True),
            preserve_default=True,
        ),
    ]
