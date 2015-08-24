# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
        ('deporte', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Titulo', models.CharField(max_length=150)),
                ('publicacion', models.TextField()),
                ('Portada', models.ImageField(upload_to=b'portadas')),
                ('Carrera', models.ForeignKey(to='inicio.Carrera')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='punto',
            name='Partidos_ganados',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='punto',
            name='anotaciones',
            field=models.IntegerField(default=0, help_text=b'Agregar todos los Puntos anotados en el partidos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='punto',
            name='recibidos',
            field=models.IntegerField(default=0, help_text=b'Agregar todos los Puntos recibidos en el partidos'),
            preserve_default=True,
        ),
    ]
