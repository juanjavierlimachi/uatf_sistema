from django.conf.urls import patterns, include, url

from .views import *#aki ay estoy importando todas las mis vistas //rolPartidos

urlpatterns = patterns('',
	#url(r'^carreras/$',Vercarreras), 
	#todlas las urls de abajo son de la aplicacionde del cliente 
	url(r'^diciplinas/$',Verdiciplinas),
	url(r'^buscar/$',buscar),
	#url(r'^rolPartidos/$', rolPartidos),
	url(r'^partidos/(?P<id>\d+)/$', partidos),
	url(r'^diciplinas/(?P<id>\d+)/$', diciplinas),
	url(r'^diciplina/(?P<iddiciplina>\d+)/carrera/(?P<idcarrera>\d+)/$', partidosRoles),
	#url(r'^diciplina/(?P<iddiciplina>\d+)/carrera/(?P<idcarrera>\d+)/$',consulta),este en prueva
	url(r'^nuevadiciplina/$',nuevadiciplina),
	url(r'^partidosRol/(?P<id>\d+)/$',partidosRol),

	url(r'^diCampeonato/(?P<id>\d+)/$',diCampeonato),
	url(r'^rolDeDiciplina/(?P<id>\d+)/campeonato/(?P<idCam>\d+)/$',rolDeDiciplina),
	url(r'^di/(?P<idd>\d+)/ca/(?P<idc>\d+)/$',rol),
	url(r'^ultimos/(?P<id>\d+)/$',ultimos),
	url(r'^ultimosIntercarrera/(?P<id>\d+)/$',ultimosIntercarrera),
	url(r'^intercarreras/$',intercarreras), 
	url(r'^inter/(?P<id>\d+)/$',intercarrerasFechas),
	url(r'^equiposCarrera/(?P<id>\d+)/diciplinas/(?P<idc>\d+)/$',equiposCarrera),
	url(r'^equiposCarreraInter/(?P<id>\d+)/diciplinasInter/(?P<idc>\d+)/$',equiposCarreraInter),
	url(r'^tablas/$',tablas),  
	url(r'^todoEquipos/$',todoEquipos),
	url(r'^publicacionesCarrera/$',publicacionesCarrera),

	url(r'^Equipos-del-Campeonato/(?P<id>\d+)/$',EquiposDeCampeonato),
) 