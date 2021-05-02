from django.db import models

class Refugio(models.Model):

    nombre = models.CharField(max_length=50)    
    direccion = models.CharField(max_length=40, verbose_name="Domicilio")
    cp = models.CharField(max_length=15,verbose_name="Código Postal")
    localidad = models.CharField(max_length=40)
    provincia = models.CharField(max_length=40)
    telefono = models.IntegerField(verbose_name="Teléfono")  
    codigoArea = models.IntegerField(verbose_name="Prefijo")
    celular = models.IntegerField(verbose_name="Celular", null=True, blank=True)
    email = models.EmailField(verbose_name="Correo electrónico", unique=True)
    confirmacionEmail = models.EmailField (verbose_name="Repita Correo electrónico")
    facebook = models.CharField(max_length=40, blank=True, null = True)
    instagram = models.CharField(max_length=40, blank=True, null = True)
    foto_refugio = models.ImageField(upload_to="refugios")
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre