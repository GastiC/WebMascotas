from django import forms
from .models import Contacto
from crispy_forms.helper import FormHelper

class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(label="Nombre") 
    apellido = forms.CharField() 
    email = forms.EmailInput()
    confirmacionEmail = forms.EmailInput()
    codigoArea = forms.IntegerField(label="Prefijo",)
    telefono = forms.IntegerField()
    celular = forms.IntegerField(label="Teléfono alternativo", required=False)
    domicilio = forms.CharField()
    localidad = forms.CharField()
    cp = forms.CharField(label="Código Postal",)
    consulta = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))

    class Meta:
        model = Contacto
        fields = '__all__'
