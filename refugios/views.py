from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

#Models
from django.contrib.auth.models import User

def asociar_un_refugio(request):

    return render(request, "refugios/asociar_un_refugio.html")
    
def adoptar_una_mascota(request):

    return render(request, "refugios/adoptar_una_mascota.html")