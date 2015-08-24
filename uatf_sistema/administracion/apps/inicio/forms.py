from django import forms
from django.forms import ModelForm
from .models import *
from administracion.apps.deporte.models import *
from django.forms.extras.widgets import SelectDateWidget

class ReCarreraform(forms.ModelForm):
	class Meta:
		model=Carrera
CHOICES = (('Inter-Carreras', 'Si',), ('Carreras', 'No(Pre-determinado)',))
class FormPartidos(forms.ModelForm):
	fecha=forms.DateField(widget=SelectDateWidget())
	Inter_carrera=forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
	class Meta:
		model=FechaPartido

GENERO = (('M', 'Mujeres',), ('V', 'Varones',))
class RolesPartidos(forms.ModelForm):
	Categoria=forms.ChoiceField(widget=forms.RadioSelect, choices=GENERO)
	class Meta:
		model=Partido

class FormDiciplinas(forms.ModelForm):
	class Meta:
		model=Diciplina
Puntaje = (('0', '0',), ('1', '1',),('2', '2',),('3', '3',))
Gano = (('0', 'Perdio',), ('1', 'Gano',),('2', 'Empato',))
class FormEquipo(forms.ModelForm):
	Puntaje=forms.ChoiceField(widget=forms.RadioSelect, choices=Puntaje)
	Partidos_ganados=forms.ChoiceField(widget=forms.RadioSelect, choices=Gano)
	class Meta:
		model=Punto
		exclude=['jugadas']
class FormEquipos(forms.ModelForm):
	class Meta:
		model=equipo

class FormPortadas(forms.ModelForm):
	class Meta:
		model=Publicacion
class FormCampeonatos(forms.ModelForm):
	Fecha_inicio=forms.DateField(widget=SelectDateWidget())
	Fecha_conclucion=forms.DateField(widget=SelectDateWidget())
	class Meta:
		model=Campeonato



		