from django.urls import path
from principal import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home),
    path('refugios/', views.refugios),    
    path('contacto/', views.contacto),
    path('preguntas_frecuentes/', views.preguntas_frecuentes),
    path('terminos_y_condiciones/', views.terminos_y_condiciones),
    path('quienes_somos/', views.quienes_somos),
    path('informacion/', views.informacion),
    path('refugios/<id>/', views.informacion_refugios)
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)