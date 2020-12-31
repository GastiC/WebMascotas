from django import forms
from .models import Busqueda

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
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    foto = forms.ImageField(label="Foto de tu mascota",)

    class Meta:
        model = Busqueda
        fields = ['nombreMascota','categoria','raza','localidad','provincia','codigoArea','telefono','celular','descripcion','foto','cp']
