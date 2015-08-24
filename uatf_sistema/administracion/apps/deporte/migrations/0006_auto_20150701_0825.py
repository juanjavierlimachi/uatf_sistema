# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
        ('deporte', '0005_auto_20150618_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre_campeonato', models.CharField(max_length=200)),
                ('Fecha_inicio', models.DateField()),
                ('Fecha_conclucion', models.DateField()),
                ('Equipo', models.ForeignKey(to='inicio.Carrera')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='diciplina',
            name='carrera',
        ),
        migrations.RemoveField(
            model_name='equipo',
            name='carrera',
        ),
        migrations.RemoveField(
            model_name='partido',
            name='Carrera',
        ),
        migrations.AddField(
            model_name='diciplina',
            name='campeonato',
            field=models.ManyToManyField(to='deporte.Campeonato'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipo',
            name='campeonato',
            field=models.ForeignKey(default=2, to='deporte.Campeonato'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partido',
            name='campeonato',
            field=models.ForeignKey(default=2, to='deporte.Campeonato'),
            preserve_default=False,
        ),
    ]
