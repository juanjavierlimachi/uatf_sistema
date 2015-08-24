# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deporte', '0003_auto_20150618_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='Fercha_publicacion',
            field=models.DateTimeField(default='2015-02-02', auto_now=True),
            preserve_default=False,
        ),
    ]
