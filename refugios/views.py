from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import RefugioForm
#Models
from django.contrib.auth.models import User

def asociar_un_refugio(request):

    refugio = RefugioForm()

    if request.method == 'POST':
        formulario = RefugioForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
        else:
            refugio = formulario

    return render(request, "refugios/asociar_un_refugio.html", {'refugio': refugio})
    
def adoptar_una_mascota(request):

    return render(request, "refugios/adoptar_una_mascota.html")