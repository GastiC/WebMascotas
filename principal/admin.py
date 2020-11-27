from django.contrib import admin
from .models import Contacto
from refugios.models import Refugio

class RefugioAdmin(admin.ModelAdmin):
    list_display = ['nombre','localidad','provincia', 'email']
    search_fields = ['nombre','localidad','provincia','email']
    list_filter = ['localidad','provincia']
    list_per_page = 10

class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido', 'localidad', 'email']
    search_fields = ['nombre','apellido', 'localidad', 'email']
    list_filter = ['localidad',]
    list_per_page = 10



admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Refugio, RefugioAdmin)
