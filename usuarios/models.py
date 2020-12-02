from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Busqueda(models.Model):
    nombreMascota = models.CharField(max_length=40)    
    categorias = models.TextChoices('categorias',['Perro','Gato'])
    categoria = models.CharField(blank=False, default="Perro", choices=categorias.choices, max_length=10)
    raza = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)
    foto = models.ImageField(upload_to="usuarios")
    creado = models.DateTimeField(auto_now_add=True)
    provincia = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    codigoArea = models.IntegerField()
    telefono = models.IntegerField()
    celular = models.IntegerField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombreMascota

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    domicilio = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    cp = models.CharField(max_length=40)
    codigoArea = models.IntegerField()
    telefono = models.IntegerField()
    celular = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    confirmacionEmail = models.EmailField()
    password = models.CharField(max_length=30)
    confirmacionPassword = models.CharField(max_length=30)

    def __str__(self):
        return self.email
