from django import forms
from django.forms import ModelForm
from .models import *
class fbuscar(forms.Form):
    texto=forms.CharField(max_length=50, label="Buscar")

class FormDiciplina(forms.ModelForm):
	class Meta:
		model=Diciplina



