from django.conf.urls import patterns, include, url

from .views import *#aki ay estoy importando todas las mis vistas //

urlpatterns = patterns('',
	url(r'^$', Usuario),
	url(r'^privado/$', ingreso, name='privado'),
	url(r'^cerrar/$', serrar),
	url(r'^datos/(?P<id>\d+)/$',Datos),
	url(r'^editar_perfil/$',editar_perfil,name='editar_perfil'),
	url(r'^nuevoUser/$',nuevoUser.as_view(), name='nuevoUser'),
)