from django import forms
from .models import Refugio

class RefugioForm(forms.ModelForm):
    nombre = forms.CharField()
    direccion = forms.CharField(label="Domicilio",) 
    email = forms.EmailInput()
    confirmacionEmail = forms.EmailInput()
    codigoArea = forms.IntegerField(label="Prefijo",)
    telefono = forms.IntegerField()
    celular = forms.IntegerField(required=False)
    localidad = forms.CharField()
    provincia = forms.CharField()
    cp = forms.CharField(label="C.P",)
    facebook = forms.CharField(required=False)
    instagram = forms.CharField(required=False)
    foto_refugio = forms.ImageField()
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))

    class Meta:
        model = Refugio
        fields = '__all__'
