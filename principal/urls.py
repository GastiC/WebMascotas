from django.urls import path

from principal import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home),
    path('busquedas/', views.busquedas),
    path('refugios/', views.refugios),    
    path('contacto/', views.contacto),
    path('preguntas_frecuentes/', views.preguntas_frecuentes),
    path('terminos_y_condiciones/', views.terminos_y_condiciones),
    path('quienes_somos/', views.quienes_somos),
    path('informacion/', views.informacion),
]