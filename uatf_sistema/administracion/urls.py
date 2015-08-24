from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'administracion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
        #las urls de mi aplicacion inicio
    url(r'^',include('administracion.apps.inicio.urls')),
    #las urls de mi aplicacion usuario
    url(r'^',include('administracion.apps.usuario.urls')),
    #las urls de mi aplicacion secretaria
    url(r'^',include('administracion.apps.secretaria.urls')),
    #las urls de mi aplicacion deporte
    url(r'^',include('administracion.apps.deporte.urls')),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',#este para optener las images de todos los uatores
        {'document_root': settings.MEDIA_ROOT, } ),
)
