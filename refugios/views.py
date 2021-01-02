from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import RefugioForm
from principal.forms import NewsletterForm
#Models
from django.contrib.auth.models import User

def asociar_un_refugio(request):
    refugio = RefugioForm()
    newsletter = NewsletterForm()
    if request.method == 'POST':
        formulario = RefugioForm(data=request.POST, files=request.FILES)
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        elif formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            refugio = formulario
            newsletter = formularioNewsletter     

    return render(request, "refugios/asociar_un_refugio.html", {'refugio': refugio, 'newsletter': newsletter})
    
def adoptar_una_mascota(request):
    newsletter = NewsletterForm()
    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            newsletter = formularioNewsletter  

    return render(request, "refugios/adoptar_una_mascota.html", {'newsletter': newsletter})