from django.shortcuts import render, render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import User
from .forms import *#aki estoy importando todos mis formularios de mi achivo form.py
from .models import *##aki estoy importando todos mis models de mi achivo models.py
# Create your views here.
from django.views.generic import TemplateView, FormView,ListView,CreateView
from django.core.urlresolvers import reverse_lazy

def Usuario(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/privado/')
	if request.method=='POST':
		formulario=AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario=request.POST['username']
			clave=request.POST['password']
			acceso=authenticate(username=usuario,password=clave)
			if acceso is not None:
				#si es el super usuario ingresa a privado
				if acceso.is_active and acceso.is_superuser and acceso.is_staff:
					login(request,acceso)
					return HttpResponseRedirect('/privado/')
				else:
					if acceso.is_active and acceso.is_staff:
						login(request,acceso)
						return HttpResponseRedirect('/privado/')
					else:
						if acceso.is_active:
							login(request,acceso)
							return HttpResponseRedirect('/privado/')
					#return render_to_response('usuario/noactivo.html',context_instance=RequestContext(request))
			else:
				return render_to_response('usuario/nousuario.html',context_instance=RequestContext(request))
	else:
		formulario=AuthenticationForm()
	return render_to_response('index.html',{'formulario':formulario},context_instance=RequestContext(request))
@login_required(login_url='/')
def ingreso(request):
	usuario=request.user
	if request.user.is_staff and request.user.is_active and request.user.is_superuser:
		#denuncias=Comment.objects.all().order_by('-id')
		return render_to_response('usuario/ingreso.html',{'usuario':usuario},context_instance=RequestContext(request))
	else:
		#user.is_staff decimoe q el administrador le dio el permiso para subsustema secretria
		if request.user.is_active and request.user.is_staff:
			return render_to_response('secretaria/inicio_secretaria.html',{'usuario':usuario},context_instance=RequestContext(request))
		else:
			if request.user.is_active:
				conogramas=Cronograma.objects.all().order_by('-id')[0:1]
				return render_to_response('inspector/inicio_inspector.html',{'usuario':usuario,'conogramas':conogramas},context_instance=RequestContext(request))

class nuevoUser(FormView):
	#usuario=request.cleaned_data['username']
	#templeta_name es para enviar un atributo form para mi formulariode registro
	template_name = 'usuario/nuevo.html'
	#con form_class indico el formularios estoy utilizando
	#model = User 
	form_class=UserForm
	success_url = reverse_lazy('privado')
	def form_valid(self,form):
		user=form.save()
		perfil=Perfiles()
		perfil.usuario = user
		#perfil.nombre=form.cleaned_data['nombre']
		perfil.ci=form.cleaned_data['ci']
		#perfil.telefono=form.cleaned_data['telefono']
		perfil.save()
		#crear_grupo=Group.objects.get_or_create(name='Cliente')
		#usuario.groups.add(usuario)
		return super(nuevoUser, self).form_valid(form)
def Datos(request,id):
	usuario=User.objects.filter(id=id)
	print usuario
	dato=Perfiles.objects.all()
	return render_to_response('usuario/datos.html',{'usuario':usuario,'dato':dato},context_instance=RequestContext(request))
 
@login_required(login_url='/')
def serrar(request):
	logout(request)
	return HttpResponseRedirect('/')
@login_required(login_url='/')
def editar_perfil(request):
	if request.method=='POST':
		user_form=UserForms(request.POST,instance=request.user)
		perfil_form=formPerfiles(request.POST,instance=request.user.perfil)
		if user_form.is_valid() and perfil_form.is_valid():
			user_form.save()
			perfil_form.save()
			return HttpResponseRedirect('/editarperfil/')
	else:
		user_form=UserForms(instance=request.user)
		perfil_form=formPerfiles(instance=request.user.perfil)
	return render_to_response('usuario/datossss.html',{'user_form':user_form,'perfil_form':perfil_form},context_instance=RequestContext(request))

