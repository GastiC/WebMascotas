from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from refugios.models import Refugio

#Models
from django.contrib.auth.models import User

def home (request):
    
    return render(request, "principal/home.html")

def busquedas(request):

    return render(request , "principal/busquedas.html")


def refugios(request):
    refugios = Refugio.objects.all()
    return render(request, "principal/refugios.html",{'refugios': refugios})

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
