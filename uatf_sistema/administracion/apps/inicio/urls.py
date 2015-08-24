from django.conf.urls import patterns, include, url

from .views import *#aki ay estoy importando todas las mis vistas

urlpatterns = patterns('',
	#url(r'^$',index.as_view()),
	url(r'^deporte/$',InicioDeporte),
	url(r'^nueCarrera/$', nueCarrera),
	#url(r'^ListaCarrera/$', ListaCarrera),
	url(r'^detalles/(?P<id>\d+)/$',Detalles),
	url(r'^Eliminar/(?P<id>\d+)/$',Eliminar),

	#urlas de las diciplinas diciplinasPorcarrera/ eliminarDiciplina
	url(r'^VerDiciplinas/$',Diciplinas),
	url(r'^busqueda_ajax/$',busquedaAjaxView.as_view(), name='buscarView'),
	url(r'^FerchaPartido/$', programarPartidoFecha),
	url(r'^nuevoRolPartidos/$', nuevoRolPartidos),

	url(r'^Asignar/(?P<id>\d+)/$',AsignarDiciCarrera),
	url(r'^eliminarDiciplina/(?P<id>\d+)/$',eliminarDiciplina),
	#url para hacer los consultas de los 
	url(r'^verIntercarreras/$',verIntercarreras),
	url(r'^informe/$', informe),
	url(r'^porferchas/$',porferchas.as_view(), name='porferchas'),
	url(r'^informe/$', informe),
	url(r'^registroEquipo/$', registroEquipo),
	url(r'^Equipos/$', Equipos),
	url(r'^registroPuntuacion/$', registroPuntuacion),
	url(r'^EquiposPor/$',EquiposPor.as_view(), name='EquiposPor'),

	url(r'^delete/(?P<id>\d+)/$',delete),
	url(r'^update/(?P<id>\d+)/$',updateEquipo),
	url(r'^deletePartido/(?P<id>\d+)/$',deletePartido),
	url(r'^updatePartido/(?P<id>\d+)/$',updatePartido),
	url(r'^Puntos/(?P<id>\d+)/$',Puntos),
	url(r'^deletePunto/(?P<id>\d+)/$',deletePunto),
	url(r'^edirPunto/(?P<id>\d+)/$',edirPunto),
	url(r'^verFechasProgramcion/$', verFechasProgramcion),
	url(r'^editFecha/(?P<id>\d+)/$',editFecha),
	url(r'^eliminarFechas/(?P<id>\d+)/$',eliminarFechas),

	url(r'^Publicaciones/$',RegistroPublicaciones.as_view(),name='RegistroPublicaciones'),
	url(r'^VerPublicaciones/$',VerPublicaciones, name='VerPublicaciones'),
	url(r'^eliminarPortada/(?P<id>\d+)/$',eliminarPortada, name='eliminarPortada'),
	url(r'^EditarPortada/(?P<id>\d+)/$',EditarPortada, name='EditarPortada'),
	
	url(r'^Campeonatos/$', Campeonatos),
	url(r'^VerCampeonatos/$', VerCampeonatos),
	url(r'^EliminarCampeonatos/(?P<id>\d+)/$',EliminarCampeonatos),
	url(r'^editCampeonatos/(?P<id>\d+)/$',editCampeonatos),
	url(r'^DicCampeonato/(?P<id>\d+)/$',DicCampeonato),
	url(r'^buscarEquipo/$',buscarEquipo),
	url(r'^EuipoId/(?P<id>\d+)/$',EuipoId), 
) 