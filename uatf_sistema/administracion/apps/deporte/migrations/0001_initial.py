# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre_diciplina', models.CharField(max_length=60)),
                ('carrera', models.ManyToManyField(to='inicio.Carrera')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre_equipo', models.CharField(max_length=70)),
                ('carrera', models.ForeignKey(help_text=b'ignore esta opcion si no corresponde a una carrera', to='inicio.Carrera')),
                ('diciplina', models.ForeignKey(to='deporte.Diciplina')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FechaPartido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lugar', models.CharField(max_length=70)),
                ('fecha', models.DateField()),
                ('Inter_carrera', models.CharField(default=b'Carreras', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora', models.CharField(max_length=8)),
                ('EquipoA', models.CharField(max_length=50)),
                ('EquipoB', models.CharField(max_length=50)),
                ('Categoria', models.CharField(max_length=2)),
                ('Carrera', models.ForeignKey(help_text=b'seleccione una carrera en el caso si es campeonato interno de una carrera', to='inicio.Carrera')),
                ('Fecha_Partido', models.ForeignKey(to='deporte.FechaPartido')),
                ('diciplina', models.ForeignKey(to='deporte.Diciplina')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Punto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Puntaje', models.IntegerField(default=0)),
                ('jugadas', models.IntegerField(default=1)),
                ('Equipo', models.ForeignKey(to='deporte.equipo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
