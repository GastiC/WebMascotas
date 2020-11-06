from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from usuarios.models import Busqueda

#Models
from django.contrib.auth.models import User

def subi_tu_post(request):

    return render(request, "usuarios/subi_tu_post.html")

def login_view(request):
   
    return render(request, "usuarios/login.html")

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
     
    return render(request, "usuarios/sign_in.html")

def reset_password(request):

    return render(request, "usuarios/reset_password.html")


def main_login(request):

    return render(request, "usuarios/main_login.html")

def change_password(request):

    return render(request, "usuarios/change_password.html")  

def mi_busqueda(request):

    return render(request, "usuarios/mi_busqueda.html")

def busquedas(request):

    busquedas = Busqueda.objects.all()
    return render(request , "usuarios/busquedas.html", {'busquedas': busquedas})