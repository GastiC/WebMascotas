from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from usuarios.models import Busqueda
from .forms import BusquedaForm, NuevoUsuarioForm
from principal.forms import NewsletterForm
#Models
from django.contrib.auth.models import User

def subi_tu_post(request):
    busqueda = BusquedaForm()
    newsletter = NewsletterForm()
    if request.method == 'POST':
        formulario = BusquedaForm(data=request.POST, files=request.FILES)
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        elif formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            busqueda = formulario
            newsletter = formularioNewsletter     

    return render(request, "usuarios/subi_tu_post.html", {'busqueda': busqueda, 'newsletter': newsletter})

def login_view(request):

    return render(request, "principal/templates/registration/login.html")

def sign_in(request):
    nuevoUsuario = NuevoUsuarioForm()
    newsletter = NewsletterForm()

    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST)
        formularioUsuario = NuevoUsuarioForm(data=request.POST)
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        elif formularioUsuario.is_valid():
            formularioUsuario.save()
            user = authenticate(username=formularioUsuario.cleaned_data['username'], password=formularioUsuario.cleaned_data['password1'])
            login(request, user)
            return redirect(to='../../main_login')
        else:
            newsletter = formularioNewsletter  
            nuevoUsuario = formularioUsuario
    return render(request, "usuarios/sign_in.html", {'newsletter': newsletter, 'nuevoUsuario': nuevoUsuario})

def reset_password(request):
    newsletter = NewsletterForm()
    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            newsletter = formularioNewsletter  

    return render(request, "usuarios/reset_password.html", {'newsletter': newsletter})


def main_login(request):
    newsletter = NewsletterForm()
    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            newsletter = formularioNewsletter  

    return render(request, "usuarios/main_login.html", {'newsletter': newsletter})

def change_password(request):
    newsletter = NewsletterForm()
    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            newsletter = formularioNewsletter  

    return render(request, "usuarios/change_password.html", {'newsletter': newsletter})  

def mi_busqueda(request):
    newsletter = NewsletterForm()
    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            newsletter = formularioNewsletter  

    return render(request, "usuarios/mi_busqueda.html", {'newsletter': newsletter})

def busquedas(request):
    newsletter = NewsletterForm()
    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            newsletter = formularioNewsletter  

    busquedas = Busqueda.objects.all()
    paginator = Paginator(busquedas, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)   
    return render(request , "usuarios/busquedas.html", {'page_obj': page_obj, 'page_number': page_number,'newsletter': newsletter})