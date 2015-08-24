from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import User
class UserForm(UserCreationForm):
	username = forms.CharField(max_length=40,required=True)
	password1 = forms.CharField(required=True)
	password2 = forms.CharField(required=True)
	first_name = forms.CharField(max_length=40,required=True)
	last_name = forms.CharField(max_length=50,required=True)
	ci = forms.IntegerField(required=True)
	#telefono = forms.IntegerField()
	class Meta:
		model=User
		fields=("username","password1","password2","first_name","last_name")
	def save(self,commit=True):
		user=super(UserForm,self).save(commit=False)
		user.first_name=self.cleaned_data.get("first_name")
		user.last_name=self.cleaned_data.get("last_name")
		if commit:
			user.save()
		return user
#formularios para editar el usuario
class formPerfiles(forms.ModelForm):
	class Meta:
		model=Perfiles
		exclude=['usuario']
class UserForms(forms.ModelForm):
	class Meta:
		model=User
		fields = ('username','first_name','last_name')
		#exclude=['password']


