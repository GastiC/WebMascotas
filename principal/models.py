from django.db import models

# Create your models here.


class Contacto(models.Model):
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50) 
    email = models.EmailField()
    confirmacionEmail = models.EmailField(verbose_name="Confirmación Email")
    codigoArea = models.IntegerField(verbose_name="Código de área")
    telefono = models.IntegerField(verbose_name="Teléfono")
    celular = models.IntegerField(null=True, blank=True)
    domicilio = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    cp = models.CharField(max_length=40, verbose_name="Código Postal")
    consulta = models.TextField()

    def __str__(self):
        return self.email

class Newsletter(models.Model):
    email_newsletter = models.EmailField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email_newsletter