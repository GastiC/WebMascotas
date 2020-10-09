from django.urls import path

from refugios import views

urlpatterns = [
    path('asociar_un_refugio/', views.asociar_un_refugio),
    path('adoptar_una_mascota/', views.adoptar_una_mascota),
]