from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from refugios.models import Refugio
from .forms import ContactoForm, NewsletterForm

#Models
from django.contrib.auth.models import User

def home (request):
    contacto = ContactoForm()
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST, prefix="contacto")
        if formulario.is_valid():
            formulario.save()
        else:
            contacto = formulario

    newsletter = NewsletterForm()
    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST, prefix="contacto")
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            newsletter = formularioNewsletter            

    
    return render(request, "principal/home.html", {'contacto': contacto,'newsletter': newsletter })

def home (request):
    contacto = ContactoForm(prefix="contacto")
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST, prefix="contacto")
        if formulario.is_valid():
            formulario.save()
        else:
            contacto = formulario

    newsletter = NewsletterForm(prefix="contacto")
    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST, prefix="contacto")
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            newsletter = formularioNewsletter            

    
    return render(request, "principal/home.html", {'contacto': contacto,'newsletter': newsletter })    

def refugios(request):
    refugios = Refugio.objects.all()
    return render(request, "principal/refugios.html",{'refugios': refugios})

def informacion_refugios(request, id):

    info_refugio = Refugio.objects.get(id=id)
    refugios = Refugio.objects.filter(id=id)
    return render(request, "principal/informacion_refugios.html", {'info_refugio': info_refugio, 'refugios': refugios})


def contacto(request):
    contacto = ContactoForm()

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            contacto = formulario



    return render(request, "principal/contacto.html", {'contacto': contacto})

#footer

def preguntas_frecuentes(request):

    return render(request, "principal/preguntas_frecuentes.html")

def terminos_y_condiciones(request):

    return render(request, "principal/terminos_y_condiciones.html")

def quienes_somos(request):

    return render(request, "principal/quienes_somos.html")    

def informacion(request):

    return render(request, "principal/informacion.html")

