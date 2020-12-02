from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-group col-md-6' }), label="Nombre") 
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-group col-md-6'})) 
    email = forms.EmailInput()
    confirmacionEmail = forms.EmailInput()
    codigoArea = forms.IntegerField(label="Código de Área",)
    telefono = forms.IntegerField()
    celular = forms.IntegerField(label="Teléfono alternativo", required=False)
    domicilio = forms.CharField()
    localidad = forms.CharField()
    cp = forms.CharField(label="Código Postal",)
    consulta = forms.TextInput()

    class Meta:
        model = Contacto
        fields = '__all__'
