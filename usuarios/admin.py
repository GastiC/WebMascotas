from django.contrib import admin
from .models import Busqueda, Usuario

class BusquedaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado',)


admin.site.register(Busqueda, BusquedaAdmin)