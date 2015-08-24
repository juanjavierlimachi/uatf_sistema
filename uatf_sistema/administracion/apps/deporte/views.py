from django.shortcuts import render,render_to_response
from administracion.apps.inicio.models import Carrera
from django.template import RequestContext
from .models import *
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
# Create your views here.
def Verdiciplinas(request):
    diciplinas=Diciplina.objects.all().distinct()
    return render_to_response('deporte/diciplinas.html',{'diciplinas':diciplinas},context_instance=RequestContext(request))
def buscar(request):
    if request.method=="POST":
        #"""Aqui ira otra busqueda igual que abajo"""
        #return HttpResponse("hecho")
        pass
    else:
        texto=request.GET["texto"]
        busqueda=(
            Q(Nombre_Carrera__icontains=texto) |
            Q(Nombre_Carrera__icontains=texto) |
            Q(Nombre_Carrera__icontains=texto)
        )
        resultados=Carrera.objects.filter(busqueda).distinct()
        html="<ul class='ul_lista'>"
        for i in resultados:
            html=html+"<li><a href='/partidosRol/"+str(i.id)+"/'>"+i.Nombre_Carrera+"</a></li>"
        html=html+"<ul>"
        return HttpResponse(html)

def partidos(request,id):
    carreras=Carrera.objects.filter(id=id)
    partidos=Partido.objects.all().order_by("-id")
    fechapartidos=FechaPartido.objects.all()
    # datos=[]
    # ultimos=FechaPartido.objects.all().order_by('-id')[0]
    # listaC=[]
    # c=Carrera.objects.get(id=id)
    # listaC.append(c)
    # datos.append(ultimos)
    return render_to_response('deporte/rolesForm.html',{'carreras':carreras,'partidos':partidos,'fechapartidos':fechapartidos},context_instance=RequestContext(request))

def diciplinas(request,id):
    diciplinas=Diciplina.objects.filter(id=id)
    carreras=Carrera.objects.all()
    return render_to_response('deporte/diciplinasPorCarrera.html',{'diciplinas':diciplinas,'carreras':carreras},context_instance=RequestContext(request))

def partidosRoles(request,iddiciplina,idcarrera):#no da
    diciplinas=Diciplina.objects.filter(id=int(iddiciplina))
    datos=[]
    ultimos=FechaPartido.objects.filter(carrera=int(idcarrera)).order_by('-id')
    datos.append(ultimos)
    partidos=Partido.objects.all().order_by('-id')
    carreras=Carrera.objects.filter(id=int(idcarrera))
    fechapartidos=FechaPartido.objects.all()

    return render_to_response('deporte/partidosPorDiciplina.html',{'datos':datos,'partidos':partidos,'diciplinas':diciplinas,'carreras':carreras,'fechapartidos':fechapartidos},context_instance=RequestContext(request))
def nuevadiciplina(request):
    if request.method=='POST':
        formulario=FormDiciplina(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario=FormDiciplina()
    return render_to_response('deporte/FormDiciplina.html',{'formulario':formulario},context_instance=RequestContext(request))
def verDciplinas(request):
    diciplinas=Diciplina.objects.all()
    return render_to_response('deporte/listaDiciplnas.html',{'diciplinas':diciplinas},context_instance=RequestContext(request))

def partidosRol(request,id): #muestro los ultimos 4 campeonatos nada mas
    carrera=Carrera.objects.get(id=int(id))
    diciplinasCarreras=Campeonato.objects.filter(Carrera=int(id)).order_by("-id")[0:4]
    return render_to_response('deporte/rol.html',{'carrera':carrera,'diciplinasCarreras':diciplinasCarreras},context_instance=RequestContext(request))

def diCampeonato(request,id):
    Nombre_campeonato=Campeonato.objects.get(id=id)
    diciplinas=Diciplina.objects.filter(campeonato=int(id)).order_by('-id')
    return render_to_response('deporte/CampeonatoDiciplina.html',{'diciplinas':diciplinas,'Nombre_campeonato':Nombre_campeonato},context_instance=RequestContext(request))

def rol(request,idd,idc):
    partidos=Partido.objects.filter(diciplina=int(idd),campeonato=int(idc)).order_by('-id')[0:1]
    estado=False
    if len(partidos)<1:
        estado=True
        dic={'estado':estado}
        print "No hay partidos"
    else:
        print partidos
    return render_to_response('deporte/sirol.html',{'partidos':partidos,'estado':estado},context_instance=RequestContext(request))
def ultimos(request,id):
    ultimafecha=FechaPartido.objects.get(id=int(id))
    partidos=Partido.objects.filter(Fecha_Partido=int(id))
    campeonato=Campeonato.objects.all()
    for c in campeonato:
        for partido in partidos:
            if partido.campeonato_id == c.id:
                #print partido.Carrera
                nombre_carrera=c.Nombre_campeonato
                break
    return render_to_response('deporte/ultimafecha.html',{'ultimafecha':ultimafecha,'partidos':partidos,'nombre_carrera':nombre_carrera},context_instance=RequestContext(request))
def ultimosIntercarrera(request,id):
    ultimafecha=FechaPartido.objects.get(id=int(id))
    partidos=Partido.objects.filter(Fecha_Partido=int(id))
    campeonato=Campeonato.objects.all()
    for c in campeonato:
        for partido in partidos:
            if partido.campeonato_id == c.id:
                #print partido.Carrera
                nombre_carrera=c.Nombre_campeonato
                break
    return render_to_response('deporte/ultimafechaIntercarrera.html',{'ultimafecha':ultimafecha,'partidos':partidos,'nombre_carrera':nombre_carrera},context_instance=RequestContext(request))
def intercarreras(request):#aki muestro los campeonatos intercarreras
    Fecha_Partido=FechaPartido.objects.all().order_by('-id')
    #print Fecha_Partido
    #diciplinas=Diciplina.objects.all()
    #Fecha_Partido=reversed(Fecha_Partido[:5])#solo muestro las ultimas 5 fechas de inter-carreras
    cam=Campeonato.objects.filter(Carrera=None).order_by('-id')[0:5]
    return render_to_response('deporte/intercarreras.html',{'cam':cam},context_instance=RequestContext(request))

def intercarrerasFechas(request,id):
    Nombre_campeonato=Campeonato.objects.get(id=id)
    partidos=Diciplina.objects.filter(campeonato=id)#muestro la diciplina del campeonato correspondiente
    return render_to_response('deporte/interPartidos.html',{'partidos':partidos,'Nombre_campeonato':Nombre_campeonato},context_instance=RequestContext(request))
def rolDeDiciplina(request,id,idCam):
    #ultimafecha=FechaPartido.objects.get(id=int(id))
    partidos=Partido.objects.filter(diciplina=int(id),campeonato=int(idCam)).order_by('-id')[0:1]
    #ultimafecha=FechaPartido.objects.get(id=int(id))
    estado=False
    if len(partidos)<1:
        estado=True
        dic={'estado':estado}
        print "No hay partidos"
    else:
        print partidos
    return render_to_response('deporte/rolesPartidosIntercarreras.html',{'partidos':partidos,'estado':estado},context_instance=RequestContext(request))

from django.db.models import Avg, Sum, Max, Min, Count
def equiposCarrera(request,id,idc):
    equipos=equipo.objects.filter(campeonato=id,diciplina=idc)
    #print equipos#hasta aki elige todas los quipos correctos
    puntos=Punto.objects.all().order_by('Equipo')
    valor=0
    vesto=[]
    est=False
    punt=0
    diccionario=[]
    g=0
    per=0
    enp=0
    anotacione=0
    rec=0
    DG=0
    aa=0
    bb=0
    datos=[]
    mayor=[]
    ab='+'
    jugados=0
    for e in equipos:
        #print e.Nombre_equipo
        vesto.append(e.Nombre_equipo)
        for p in puntos:
            if e.id == p.Equipo_id:
                punt=p.Puntaje+punt
                #print 'PuntajeTotalll',punt
                jugados=Punto.objects.filter(Equipo=e.id).count()
                #print 'partidos jugados',jugados#hasta aki esta bien

                if  e.id == p.Equipo_id and p.Partidos_ganados == 1:
                    g=g+1
                    #print 'gano partidos',g
                if e.id == p.Equipo_id and p.Partidos_ganados == 2:
                    enp=enp+1
                    #print 'enpato Partidos',enp
                if e.id == p.Equipo_id and p.Partidos_ganados == 0:
                    per=per+1
                    #print 'Perdio Partidos',per
                anotacione=anotacione+p.anotaciones
                rec=rec+p.recibidos
        #print 'Anotaciones',anotacione
        #print 'recibio anotaciones:',rec
        #print 'esto es el promedio',DG
        DG=int(+anotacione)-int(rec)

        if DG>1:
            ab='+'
        if DG<0:
            ab=''
        if DG==0:
            ab=''
        diccionario.append(dict([(e.Nombre_equipo,punt)]))
        mayor.append(dict([(e.Nombre_equipo,['Pts:',punt,'PJ:',jugados,'PG:',g,'PE:',enp,'PP:',per,'GF:',anotacione,'GC:',rec,'DG:',ab,DG])]))
        valor=punt
        punt=0
        anotacione=0
        rec=0
        DG=0
        g=0
        enp=0
        per=0
        jugados=0
    print mayor
    return render_to_response('deporte/equipos.html',{'mayor':mayor,'diccionario':diccionario,'equipos':equipos,'puntos':puntos,'punt':punt,'valor':valor,'vesto':vesto},context_instance=RequestContext(request))

def equiposCarreraInter(request,id,idc):
    equipos=equipo.objects.filter(campeonato=id,diciplina=idc)
    #print equipos#hasta aki elige todas los quipos correctos
    puntos=Punto.objects.all().order_by('Equipo')
    valor=0
    vesto=[]
    est=False
    punt=0
    diccionario=[]
    g=0
    per=0
    enp=0
    anotacione=0
    rec=0
    DG=0
    aa=0
    bb=0
    datos=[]
    mayor=[]
    ab='+'
    jugados=0
    for e in equipos:
        #print e.Nombre_equipo
        vesto.append(e.Nombre_equipo)
        for p in puntos:
            if e.id == p.Equipo_id:
                punt=p.Puntaje+punt
                #print 'PuntajeTotalll',punt
                jugados=Punto.objects.filter(Equipo=e.id).count()
                #print 'partidos jugados',jugados#hasta aki esta bien

                if  e.id == p.Equipo_id and p.Partidos_ganados == 1:
                    g=g+1
                    #print 'gano partidos',g
                if e.id == p.Equipo_id and p.Partidos_ganados == 2:
                    enp=enp+1
                    #print 'enpato Partidos',enp
                if e.id == p.Equipo_id and p.Partidos_ganados == 0:
                    per=per+1
                    #print 'Perdio Partidos',per
                anotacione=anotacione+p.anotaciones
                rec=rec+p.recibidos
        #print 'Anotaciones',anotacione
        #print 'recibio anotaciones:',rec
        #print 'esto es el promedio',DG
        DG=int(+anotacione)-int(rec)

        if DG>1:
            ab='+'
        if DG<0:
            ab=''
        if DG==0:
            ab=''
        diccionario.append(dict([(e.Nombre_equipo,punt)]))
        mayor.append(dict([(e.Nombre_equipo,['Pts:',punt,'PJ:',jugados,'PG:',g,'PE:',enp,'PP:',per,'GF:',anotacione,'GC:',rec,'DG:',ab,DG])]))
        valor=punt
        punt=0
        anotacione=0
        rec=0
        DG=0
        g=0
        enp=0
        per=0
        jugados=0
    print mayor
    return render_to_response('deporte/equiposInter.html',{'mayor':mayor,'diccionario':diccionario,'equipos':equipos,'puntos':puntos,'punt':punt,'valor':valor,'vesto':vesto},context_instance=RequestContext(request))

def tablas(request):
    Inter=equipo.objects.filter(carrera_id=None)
    puntos=Punto.objects.all()
    aux=0
    punto=[]

    jugados=0
    g=0
    per=0
    enp=0
    anotacione=0
    rec=0
    DG=0
    ab='+'
    for e in Inter:
        #if e.carrera_id==None:
        #print e.Nombre_equipo#hasta aki imprimo bien los equipos de intercarrera
        for p in puntos:
            if e.id == p.Equipo_id:
                aux=p.Puntaje+aux
                #jugados=jugados+1
                #print 'Partidos Jugados',jugados
                jugados=Punto.objects.filter(Equipo=e.id).count()
                #print 'jugados:',jugados
                if  p.Partidos_ganados == 1:
                    g=g+1
                    #print 'gano partidos',g
                if p.Partidos_ganados == 2:
                        enp=enp+1
                    #print 'enpato Partidos',enp
                if p.Partidos_ganados == 0:
                    per=per+1
                    #print 'Perdio Partidos',per
                anotacione=anotacione+p.anotaciones
                rec=rec+p.recibidos

        DG=int(+anotacione)-int(rec)
        if DG>1:
            ab='+'
        if DG<0:
            ab=''
        if DG==0:
            ab=''
            #punto.append(dict([(e.Nombre_equipo,aux)]))
        punto.append(dict([(e.Nombre_equipo,['Pts:',aux,'PJ:',jugados,'PG:',g,'PE:',enp,'PP:',per,'GF:',anotacione,'GC:',rec,'DG:',ab,DG])]))
        #print punto
        aux=0
        anotacione=0
        rec=0
        DG=0
        g=0
        enp=0
        per=0
        jugados=0
    return render_to_response('deporte/posicionesInterCarreras.html',{'Inter':Inter,'punto':punto},context_instance=RequestContext(request))

def todoEquipos(request):
    todos=Campeonato.objects.all().order_by('-id')[0:20]
    t=equipo.objects.all().count()
    return render_to_response('deporte/todosLosEquipos.html',{'todos':todos,'t':t},context_instance=RequestContext(request))

def publicacionesCarrera(request):
    portadas=Publicacion.objects.all().order_by('-id')[0:20]
    numero=Publicacion.objects.all().count()

    return render_to_response('deporte/PublicaionesCarrera.html',{'portadas':portadas,'numero':numero},context_instance=RequestContext(request))

def EquiposDeCampeonato(request,id):
    nom=Campeonato.objects.get(id=int(id))
    eq=equipo.objects.filter(campeonato=int(id))
    return render_to_response('deporte/EquiposDelCampeonato.html',{'eq':eq,'nom':nom},context_instance=RequestContext(request))

