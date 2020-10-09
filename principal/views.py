from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

#Models
from django.contrib.auth.models import User

def home (request):
    
    return render(request, "home.html")

def busquedas(request):

    return render(request , "busquedas.html")


def refugios(request):

    return render(request, "refugios.html")

def contacto(request):

    return render(request, "contacto.html")

#footer

def preguntas_frecuentes(request):

    return render(request, "footer/preguntas_frecuentes.html")

def terminos_y_condiciones(request):

    return render(request, "footer/terminos_y_condiciones.html")

def quienes_somos(request):

    return render(request, "footer/quienes_somos.html")    

def informacion(request):

    return render(request, "informacion.html")
