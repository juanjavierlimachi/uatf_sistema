from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView, FormView
from .models import *
from .forms import *
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from administracion.apps.deporte.models import *
from django.views.generic import CreateView
# Create your views here.
#class index(TemplateView):
	#template_name='index.html'
def InicioDeporte(request):
	#return render_to_response('inicio/inicio_deportes.html')
	diciplinas=Diciplina.objects.all().order_by("-id")#ordenamos la lista alfabeticamente
	carrera = Carrera.objects.all().order_by("-id")
	return render_to_response('deporte.html',{'carrera':carrera,'diciplinas':diciplinas},context_instance=RequestContext(request))

def nueCarrera(request):
	contexto=request.user#asi optengo el nombre del usuer para llevar ami templte carrera.html
	print contexto
	carr=Carrera.objects.all()
	if request.method=='POST':
		formulario=ReCarreraform(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/nueCarrera/')
			#return HttpResponseRedirect('ListaCarrera')
	else:
		formulario=ReCarreraform()

	return render_to_response('inicio/carrera.html',{'contexto':contexto,'formulario':formulario,'carr':carr},context_instance=RequestContext(request))
# def ListaCarrera(request):
# 	carreras=Carrera.objects.all()
# 	return render_to_response('inicio/Lista_carrera.html',{'carreras':carreras},context_instance=RequestContext(request))

def Detalles(request,id):
	return render_to_response('inicio/detalles.html',{},context_instance=RequestContext(request))
def Eliminar(request,id):
	selec=Carrera.objects.get(id=id)
	selec.delete()
	return HttpResponseRedirect('/nueCarrera/')
def Diciplinas(request):
	diciplinas=Diciplina.objects.all().order_by('Nombre_diciplina')
	cont=Diciplina.objects.all().count()
	campeonato=Campeonato.objects.all()
	return render_to_response('inicio/diciplina.html',{'diciplinas':diciplinas,'campeonato':campeonato,'cont':cont},context_instance=RequestContext(request))

from django.core import serializers
class busquedaAjaxView(TemplateView):
	def get(self, request, *args, **kwargs):
		id_carrera = request.GET['id']
		diciplinas = Diciplina.objects.filter(campeonato=id_carrera).order_by('Nombre_diciplina')
		data = serializers.serialize('json', diciplinas,fields=('Nombre_diciplina'))
		return HttpResponse(data, 'application/json')

def programarPartidoFecha(request):
	if request.method=='POST':
		formulario=FormPartidos(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/nuevoRolPartidos/')
	else:
		formulario=FormPartidos()
	return render_to_response("inicio/rolPartidos.html",{'formulario':formulario},context_instance=RequestContext(request))

def nuevoRolPartidos(request):
	if request.method=='POST':
		formulario=RolesPartidos(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/nuevoRolPartidos/')
	else:
		formulario=RolesPartidos()
	return render_to_response("inicio/rolPartidosForm.html",{'formulario':formulario},context_instance=RequestContext(request))

def AsignarDiciCarrera(request,id):
	dato=Diciplina.objects.get(id=id)
	if request.method=='POST':
		forms=FormDiciplinas(request.POST,instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/VerDiciplinas/')
	else:
		forms=FormDiciplinas(instance=dato)
	return render_to_response('inicio/asignaciondiciplina.html',{'forms':forms},context_instance=RequestContext(request))

def eliminarDiciplina(request,id):
	dato=Diciplina.objects.get(id=id)
	dato.delete()
	return HttpResponseRedirect('/VerDiciplinas/')
def verIntercarreras(request):
	partidos=Partido.objects.all().order_by('-id')[0:100]
	campeonato=Campeonato.objects.all().order_by('-id')
	fechas=FechaPartido.objects.all().order_by('-id')
	return render_to_response('inicio/informeIntercarreras.html',{'fechas':fechas,'partidos':partidos,'campeonato':campeonato},context_instance=RequestContext(request))
def informe(request):
	partidos=Partido.objects.all().order_by('-id')[0:100]
	#print 'orogen',partidos
	#partidos=reversed(partidos[:10])#optengo las 10 ultimas fechas para mostrar el el template
	#print 'Invertido',partidos
	campeonato=Campeonato.objects.all().order_by('-id')
	fechas=FechaPartido.objects.all().order_by('-id')
	return render_to_response('inicio/informe.html',{'fechas':fechas,'partidos':partidos,'campeonato':campeonato},context_instance=RequestContext(request))
class porferchas(TemplateView):
	def get(self, request, *args, **kwargs):
		id_fecha = request.GET['id']
		print id_fecha
		partidosF = Partido.objects.filter(Fecha_Partido=id_fecha)
		data = serializers.serialize('json', partidosF,fields=('hora','EquipoA','EquipoB','diciplina'))
		return HttpResponse(data, 'application/json')

def registroPuntuacion(request):
	if request.method=='POST':
		formulario=FormEquipo(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/registroPuntuacion/')
	else:
		formulario=FormEquipo()
	return render_to_response('inicio/Equipos.html',{'formulario':formulario},context_instance=RequestContext(request))
def Equipos(request):
	Equipos=equipo.objects.all().order_by('-id')[0:100]#solo voy ha mostrar los ultimos 100 equipos
	campeonato=Campeonato.objects.all().order_by('Nombre_campeonato')
	return render_to_response('inicio/EquiposPorCarrera.html',{'campeonato':campeonato,'Equipos':Equipos},context_instance=RequestContext(request))

def registroEquipo(request):#vista q registra equipo
	if request.method=='POST':
		registroEquipo=FormEquipos(request.POST)
		if registroEquipo.is_valid():
			registroEquipo.save()
			return HttpResponseRedirect('/registroEquipo/')
	else:
		registroEquipo=FormEquipos()
	return render_to_response('inicio/registroEquipoform.html',{'registroEquipo':registroEquipo},context_instance=RequestContext(request))

class EquiposPor(TemplateView):
	def get(self, request, *args, **kwargs):
		id_carrera = request.GET['id']
		equipos = equipo.objects.filter(campeonato=id_carrera)
		data = serializers.serialize('json', equipos,fields=('Nombre_equipo'))
		return HttpResponse(data, 'application/json')
def delete(request,id):
	eq=equipo.objects.get(id=id)
	eq.delete()
	return HttpResponseRedirect('/Equipos/')

def updateEquipo(request,id):
	dato=equipo.objects.get(id=id)
	if request.method=='POST':
		forms=FormEquipos(request.POST,instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/Equipos/')
	else:
		forms=FormEquipos(instance=dato)
	return render_to_response('inicio/editarEquipo.html',{'forms':forms},context_instance=RequestContext(request))

def deletePartido(request, id):
	par=Partido.objects.get(id=id)
	par.delete()
	return HttpResponseRedirect('/informe/')

def updatePartido(request,id):
	dato=Partido.objects.get(id=id)
	if request.method=='POST':
		forms=RolesPartidos(request.POST,instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/informe/')
	else:
		forms=RolesPartidos(instance=dato)
	return render_to_response('inicio/editarPartido.html',{'forms':forms},context_instance=RequestContext(request))

def Puntos(request,id):
	et=equipo.objects.get(id=id)
	punto=Punto.objects.filter(Equipo=id).order_by('-id')
	jugados=Punto.objects.filter(Equipo=id).count()
	cont=0
	anotacion=0
	rec=0
	ganados=0
	perdidos=0
	enpatedos=0
	DG=0
	for j in punto:
		cont=j.Puntaje+cont
		anotacion=anotacion+j.anotaciones
		rec=rec+j.recibidos
		if j.Partidos_ganados == 1:
			ganados=ganados+1
		if j.Partidos_ganados == 0:
			perdidos=perdidos+1
		if j.Partidos_ganados == 2:
			enpatedos=enpatedos+1
	DG=anotacion-rec
	print cont
	return render_to_response('inicio/Puntos.html',{'et':et,'punto':punto,'cont':cont,'jugados':jugados,
		           'ganados':ganados,'enpatedos':enpatedos,'perdidos':perdidos,'anotacion':anotacion,'rec':rec,'DG':DG},context_instance=RequestContext(request))
def deletePunto(request,id):
	punto=Punto.objects.get(id=id)
	punto.delete()
	return HttpResponseRedirect('/')

def edirPunto(request,id):
	dato=Punto.objects.get(id=id)
	nun=int(id)
	if request.method=='POST':
		forms=FormEquipo(request.POST,instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms=FormEquipo(instance=dato)
	return render_to_response('inicio/editarPuntos.html',{'forms':forms},context_instance=RequestContext(request))

def verFechasProgramcion(request):
	fechas=FechaPartido.objects.all().order_by('-id')
	return render_to_response('inicio/VerFechas.html',{'fechas':fechas},context_instance=RequestContext(request))

def editFecha(request,id):
	dato=FechaPartido.objects.get(id=id)
	if request.method=='POST':
		forms=FormPartidos(request.POST,instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms=FormPartidos(instance=dato)
	return render_to_response('inicio/editarFechaPartidos.html',{'forms':forms},context_instance=RequestContext(request))

def eliminarFechas(request,id):
	fecha=FechaPartido.objects.get(id=id)
	fecha.delete()
	return HttpResponseRedirect('/verFechasProgramcion/')

def VerPublicaciones(request):
	ps=Publicacion.objects.all().order_by('-id')[0:50]
	return render_to_response('inicio/Verportadas.html',{'ps':ps},context_instance=RequestContext(request))

class RegistroPublicaciones(CreateView):
	template_name='inicio/portadas.html'
	model=Publicacion
	success_url = reverse_lazy('VerPublicaciones')


def eliminarPortada(request,id):
	por=Publicacion.objects.get(id=id)
	por.delete()
	return HttpResponseRedirect('/VerPublicaciones/')

def EditarPortada(request,id):
	port=Publicacion.objects.get(id=id)
	if request.method=='POST':
		forms=FormPortadas(request.POST,instance=port)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/VerPublicaciones/')
	else:
		forms=FormPortadas(instance=port)
	return render_to_response('inicio/editarPortadas.html',{'forms':forms},context_instance=RequestContext(request))

def Campeonatos(request):
	if request.method=='POST':
		forms=FormCampeonatos(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/VerCampeonatos/')
	else:
		forms=FormCampeonatos()
	return render_to_response('inicio/registroCampeonato.html',{'forms':forms},context_instance=RequestContext(request))

def VerCampeonatos(request):
	con=Campeonato.objects.count()
	cam=Campeonato.objects.all().order_by('-id')[0:50]
	return render_to_response('inicio/verCampeonato.html',{'cam':cam,'con':con},context_instance=RequestContext(request))

def EliminarCampeonatos(request,id):
	c=Campeonato.objects.get(id=id)
	c.delete()
	return HttpResponseRedirect('/VerCampeonatos/')
def editCampeonatos(request,id):
	port=Campeonato.objects.get(id=id)
	if request.method=='POST':
		forms=FormCampeonatos(request.POST,instance=port)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/VerCampeonatos/')
	else:
		forms=FormCampeonatos(instance=port)
	return render_to_response('inicio/editarCampeonatos.html',{'forms':forms},context_instance=RequestContext(request))

def DicCampeonato(request,id):
	pass

def buscarEquipo(request):
    if request.method=="POST":
        #"""Aqui ira otra busqueda igual que abajo"""
        #return HttpResponse("hecho")
        pass
    else:
        texto=request.GET["texto"]
        # busqueda=(
        #     Q(Nombre_equipo__icontains=texto) |
        #     Q(Nombre_equipo__icontains=texto) |
        #     Q(Nombre_equipo__icontains=texto)
        # )
        # resultados=equipo.objects.filter(busqueda).distinct()
        # print 'RESULT',resultados
        resultados=equipo.objects.filter(Nombre_equipo__icontains=texto).distinct()
        print resultados
        html="<ul class='ul_lista'>"
        for i in resultados:
            html=html+"<li><a href='/EuipoId/"+str(i.id)+"/'>"+i.Nombre_equipo+"</a></li>"
        html=html+"<ul>"
        return HttpResponse(html)

def EuipoId(request,id):
	e=equipo.objects.get(id=id)
	lista=[]
	cont=0
	puntos=Punto.objects.filter(Equipo=id)
	for i in puntos:
		lista.append(i.Puntaje)
		cont=cont+i.Puntaje
	return render_to_response('inicio/detalleEquipoId.html',{'e':e,'cont':cont,'lista':lista},context_instance=RequestContext(request))