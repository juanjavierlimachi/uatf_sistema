# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deporte', '0006_auto_20150701_0825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campeonato',
            old_name='Equipo',
            new_name='Carrera',
        ),
    ]
