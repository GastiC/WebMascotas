from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from refugios.models import Refugio
from .forms import ContactoForm, NewsletterForm
from django.core.paginator import Paginator


#Models
from django.contrib.auth.models import User


def home (request):
    contacto = ContactoForm()
    newsletter = NewsletterForm()
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        elif formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            contacto = formulario
            newsletter = formularioNewsletter     

    return render(request, "principal/home.html", {'contacto': contacto,'newsletter': newsletter})

def newsletter(request):

    newsletter = NewsletterForm()
    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            newsletter = formularioNewsletter     

    return render(request, "principal/newsletter.html", {'newsletter': newsletter })


def refugios(request):
    refugios = Refugio.objects.all() 
    newsletter = NewsletterForm()
    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            newsletter = formularioNewsletter 

    paginator = Paginator(refugios, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)   

    return render(request, "principal/refugios.html",{'page_obj': page_obj, 'page_number': page_number,'refugios': refugios,'newsletter': newsletter})

def informacion_refugios(request, id):
    info_refugio = Refugio.objects.get(id=id)
    refugios = Refugio.objects.filter(id=id)

    newsletter = NewsletterForm()
    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            newsletter = formularioNewsletter  

    return render(request, "principal/informacion_refugios.html", {'info_refugio': info_refugio, 'refugios': refugios,'newsletter': newsletter})

def contacto(request):
    contacto = ContactoForm()
    newsletter = NewsletterForm()
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        elif formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            contacto = formulario
            newsletter = formularioNewsletter     

    return render(request, "principal/contacto.html", {'contacto': contacto, 'newsletter': newsletter})

#footer

def preguntas_frecuentes(request):
    newsletter = NewsletterForm()
    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            newsletter = formularioNewsletter  

    return render(request, "principal/preguntas_frecuentes.html", {'newsletter': newsletter })

def terminos_y_condiciones(request):
    newsletter = NewsletterForm()
    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            newsletter = formularioNewsletter  

    return render(request, "principal/terminos_y_condiciones.html", {'newsletter': newsletter })

def quienes_somos(request):
    newsletter = NewsletterForm()
    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            newsletter = formularioNewsletter  

    return render(request, "principal/quienes_somos.html", {'newsletter': newsletter })    

def informacion(request):
    newsletter = NewsletterForm()
    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            newsletter = formularioNewsletter  

    return render(request, "principal/informacion.html", {'newsletter': newsletter })

