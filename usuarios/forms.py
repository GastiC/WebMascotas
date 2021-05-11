from django import forms
from .models import Busqueda, Usuario
from django.contrib.auth.forms import UserCreationForm


class BusquedaForm(forms.ModelForm):
    nombreMascota = forms.CharField(widget=forms.TextInput(), label= 'Nombre de tu mascota', max_length=50) 
    especies = [('Perro', 'Perro'),('Gato','Gato')]
    categoria = forms.ChoiceField(label="Especie", choices=especies)
    raza = forms.CharField(max_length=30,)
    localidad = forms.CharField(max_length=30,)
    provincia = forms.CharField(max_length=30,)
    cp = forms.CharField(label="C.P",)
    codigoArea = forms.IntegerField(label="Prefijo",)
    telefono = forms.IntegerField(label="Teléfono",)
    celular = forms.IntegerField(label="Teléfono alternativo", required=False)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows':5}),max_length=150,)
    foto = forms.ImageField(label="Foto de tu mascota",)

    class Meta:
        model = Busqueda
        fields = ['nombreMascota','categoria','raza','localidad','provincia','codigoArea','telefono','celular','descripcion','foto','cp']

class NuevoUsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','email','confirmacionEmail','username','password1','password2']
        help_texts = {
            'username': None,
            'email': None,
        }


