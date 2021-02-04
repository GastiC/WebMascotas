from django import forms
from .models import Busqueda
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BusquedaForm(forms.ModelForm):
    nombreMascota = forms.CharField(widget=forms.TextInput(), label= 'Nombre de tu mascota') 
    especies = [('Perro', 'Perro'),('Gato','Gato')]
    categoria = forms.ChoiceField(label="Especie", choices=especies)
    raza = forms.CharField()
    localidad = forms.CharField()
    provincia = forms.CharField()
    cp = forms.CharField(label="C.P",)
    codigoArea = forms.IntegerField(label="Prefijo",)
    telefono = forms.IntegerField(label="Teléfono",)
    celular = forms.IntegerField()
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows':5}),max_length=150,)
    foto = forms.ImageField(label="Foto de tu mascota",)

    class Meta:
        model = Busqueda
        fields = ['nombreMascota','categoria','raza','localidad','provincia','codigoArea','telefono','celular','descripcion','foto','cp']

class nuevoUsuario(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email','password1','password2']
