from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-group col-md-6' })) 
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-group col-md-6'})) 
    email = forms.EmailInput()
    confirmacionEmail = forms.EmailInput()
    codigoArea = forms.IntegerField()
    telefono = forms.IntegerField()
    celular = forms.IntegerField()
    domicilio = forms.CharField()
    localidad = forms.CharField()
    cp = forms.CharField()
    consulta = forms.TextInput()

    class Meta:
        model = Contacto
        fields = '__all__'
