from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username,  nombre, apellido,confirmacionEmail, password=None):
        if not email:
            raise ValueError('Los usuarios deben cargar un correo electrónico') 
        if not confirmacionEmail:
            raise ValueError('Los usuarios deben confirmar el correo electrónico')
        if not username:
            raise ValueError('Los usuarios deben cargar un nombre de usuario')
        if not nombre:
            raise ValueError('Los usuarios deben cargar un nombre')        
        if not apellido:
            raise ValueError('Los usuarios deben cargar un apellido')
      
        usuario = self.model(
            email = self.normalize_email(email),
            username = username,
            nombre = nombre,
            apellido = apellido,
            confirmacionEmail = self.normalize_email(confirmacionEmail),
        )

        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, username, password, nombre,apellido,confirmacionEmail):      
        usuario = self.create_user(
            email = self.normalize_email(email),
            confirmacionEmail = self.normalize_email(confirmacionEmail),
            password=password,
            username = username,
            nombre = nombre,
            apellido = apellido,
        )

        usuario.is_admin = True
        usuario.is_staff = True
        usuario.is_superuser = True        
        usuario.save(using=self._db)
        return usuario    

class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=60, unique=True)
    confirmacionEmail = models.EmailField(verbose_name="Email (confirmación)")
    username = models.CharField(max_length=40, unique=True, verbose_name="Usuario")
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username','nombre','apellido','confirmacionEmail',]

    objects = UsuarioManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

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
    cp = models.CharField(max_length=15,verbose_name="Código Postal")
    codigoArea = models.IntegerField()
    telefono = models.IntegerField()
    celular = models.IntegerField(null=True, blank=True)
    usuario_busqueda = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreMascota