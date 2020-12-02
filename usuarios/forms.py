from django import forms
from .models import Busqueda

class BusquedaForm(forms.ModelForm):
    nombreMascota = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-group col-md-6' }), label= 'Nombre de tu mascota') 
    especies = [('Perro', 'Perro'),('Gato','Gato')]
    categoria = forms.ChoiceField(label="Especie", choices=especies)
    raza = forms.CharField()
    localidad = forms.CharField()
    provincia = forms.CharField()
    codigoArea = forms.IntegerField()
    telefono = forms.IntegerField()
    celular = forms.IntegerField()
    descripcion = forms.CharField(widget=forms.Textarea)
    foto = forms.ImageField()

    class Meta:
        model = Busqueda
        fields = ['nombreMascota','categoria','raza','localidad','provincia','codigoArea','telefono','celular','descripcion','foto']
