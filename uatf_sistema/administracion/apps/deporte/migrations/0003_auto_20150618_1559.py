# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deporte', '0002_auto_20150618_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='publicacion',
            field=models.TextField(null=True, blank=True),
        ),
    ]
