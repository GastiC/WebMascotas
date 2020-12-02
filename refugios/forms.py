from django import forms
from .models import Refugio

class RefugioForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-group col-md-6' })) 
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-group col-md-6'})) 
    email = forms.EmailInput()
    confirmacionEmail = forms.EmailInput()
    codigoArea = forms.IntegerField()
    telefono = forms.IntegerField()
    celular = forms.IntegerField()
    domicilio = forms.CharField()
    localidad = forms.CharField()
    provincia = forms.CharField()
    cp = forms.CharField()
    facebook = forms.CharField()
    instagram = forms.CharField()
    foto_refugio = forms.ImageField()
    descripcion = forms.TextInput()

    class Meta:
        model = Refugio
        fields = '__all__'
