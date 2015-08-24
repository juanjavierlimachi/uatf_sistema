#encoding:utf-8
from django.db import models
from administracion.apps.inicio.models import Carrera


# Create your models here.
class Campeonato(models.Model):
	Nombre_campeonato=models.CharField(max_length=200)
	Fecha_inicio=models.DateField()
	Fecha_conclucion=models.DateField()
	Carrera=models.ForeignKey(Carrera,blank=True,null=True,help_text='Ignore esta opcion si es un Campeonato Intercarreras')
	#Portada=models.ImageField(upload_to='campeonatos')
	def __unicode__(self):
		return self.Nombre_campeonato

class Diciplina(models.Model):
	Nombre_diciplina=models.CharField(max_length=60)
	campeonato=models.ManyToManyField(Campeonato)

	def __unicode__(self):
		return self.Nombre_diciplina

class equipo(models.Model):
	Nombre_equipo=models.CharField(max_length=70)
	campeonato=models.ForeignKey(Campeonato)
	diciplina=models.ForeignKey(Diciplina)
	def __unicode__(self):
		return self.Nombre_equipo
#null=True,blank=True,
class FechaPartido(models.Model):
	lugar=models.CharField(max_length=70)
	fecha=models.DateField()
	Inter_carrera=models.CharField(max_length=100,default='Carreras')
	def __unicode__(self):
		return "%s"%self.fecha

class Partido(models.Model):
	hora=models.CharField(max_length=8)
	EquipoA=models.CharField(max_length=50)
	EquipoB=models.CharField(max_length=50)
	campeonato=models.ForeignKey(Campeonato)
	Categoria=models.CharField(max_length=2)
	Fecha_Partido=models.ForeignKey(FechaPartido)
	diciplina=models.ForeignKey(Diciplina)

class Punto(models.Model):
	Puntaje=models.IntegerField(default=0)
	Equipo=models.ForeignKey(equipo)
	jugadas=models.IntegerField(default=1)
	anotaciones=models.IntegerField(default=0,help_text='Agregar todos los Puntos anotados en el partidos')
	recibidos=models.IntegerField(default=0,help_text='Agregar todos los Puntos recibidos en el partidos')
	Partidos_ganados=models.IntegerField(default=0)#aki se guardara los partios entatados y perdidos
	#fecha_registro=models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "%s"%self.Equipo

class Publicacion(models.Model):
	Carrera=models.ForeignKey(Carrera)
	Titulo=models.CharField(max_length=150)
	publicacion=models.TextField(null=True,blank=True)
	Portada=models.ImageField(upload_to='portadas')
	Fercha_publicacion=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.publicacion
