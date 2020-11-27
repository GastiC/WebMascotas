from django.db import models

class Refugio(models.Model):

    nombre = models.CharField(max_length=50)    
    direccion = models.CharField(max_length=40)
    cp = models.IntegerField(verbose_name="Código Postal")
    localidad = models.CharField(max_length=40)
    provincia = models.CharField(max_length=40)
    tel = models.IntegerField(verbose_name="Teléfono")  
    email = models.EmailField(verbose_name="Correo electrónico")
    email_again = models.EmailField (verbose_name="Correo electrónico confirmado")
    facebook = models.CharField(max_length=40, blank=True, null = True)
    instagram = models.CharField(max_length=40, blank=True, null = True)
    foto_refugio = models.ImageField(upload_to="refugios")
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre