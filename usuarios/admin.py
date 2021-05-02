from django.contrib import admin
from .models import Busqueda, Usuario

class BusquedaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado',)
    list_display = ['nombreMascota','categoria','usuario_busqueda','creado']
    search_fields = ['nombreMascota','localidad','provincia']
    list_filter = ['categoria',]
    list_per_page = 10


class UsuarioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Busqueda, BusquedaAdmin)


admin.site.register(Usuario, UsuarioAdmin)