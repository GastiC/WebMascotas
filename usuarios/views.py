from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from usuarios.models import Busqueda
from .forms import BusquedaForm
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

    newsletter = NewsletterForm()
    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            newsletter = formularioNewsletter  

    return render(request, "usuarios/login.html",{'newsletter': newsletter})

def sign_in(request):

    """if request.method == 'POST':
        username = request.POST ['nombre']
        apellido = request.POST ['apellido']
        direccion = request.POST ['direccion']
        localidad = request.POST ['localidad']
        cp = request.POST ['cp']
        email = request.POST ['email']
        email_again = request.POST ['email_again']
        password = request.POST ['password']
        password_confirmation = request.POST ['password_confirmation']

        if password == password_confirmation:
            user = User.object.create_user(username= email, password= password)
            user.save()

            usuario = Usuario(user=user)
            usuario.save()
            

            return render(request, 'login/main_login.html',)

        else:
            return render(request, 'login/sign_in.html', {'error': 'Las contraseñas no coinciden'})"""

    newsletter = NewsletterForm()
    if request.method == 'POST':
        formularioNewsletter = NewsletterForm(data=request.POST)
        if formularioNewsletter.is_valid():
            formularioNewsletter.save()
        else:
            newsletter = formularioNewsletter  

    return render(request, "usuarios/sign_in.html", {'newsletter': newsletter})

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