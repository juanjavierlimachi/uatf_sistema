# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deporte', '0007_auto_20150701_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campeonato',
            name='Carrera',
            field=models.ForeignKey(blank=True, to='inicio.Carrera', help_text=b'Ignore esta opcion si es un Campeonato Intercarreras', null=True),
        ),
    ]
