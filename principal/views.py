from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from refugios.models import Refugio

#Models
from django.contrib.auth.models import User

def home (request):
    
    return render(request, "principal/home.html")

def refugios(request):
    refugios = Refugio.objects.all()
    return render(request, "principal/refugios.html",{'refugios': refugios})

def informacion_refugios(request, id):

    info_refugio = Refugio.objects.get(id=id)
    refugios = Refugio.objects.filter(id=id)
    return render(request, "principal/informacion_refugios.html", {'info_refugio': info_refugio, 'refugios': refugios})


def contacto(request):

    return render(request, "principal/contacto.html")

#footer

def preguntas_frecuentes(request):

    return render(request, "principal/preguntas_frecuentes.html")

def terminos_y_condiciones(request):

    return render(request, "principal/terminos_y_condiciones.html")

def quienes_somos(request):

    return render(request, "principal/quienes_somos.html")    

def informacion(request):

    return render(request, "principal/informacion.html")

