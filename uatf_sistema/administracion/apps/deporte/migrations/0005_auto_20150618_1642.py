# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deporte', '0004_publicacion_fercha_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='carrera',
            field=models.ForeignKey(blank=True, to='inicio.Carrera', help_text=b'ignore esta opcion si no corresponde a una carrera', null=True),
        ),
        migrations.AlterField(
            model_name='partido',
            name='Carrera',
            field=models.ForeignKey(blank=True, to='inicio.Carrera', help_text=b'seleccione una carrera en el caso si es campeonato interno de una carrera', null=True),
        ),
    ]
