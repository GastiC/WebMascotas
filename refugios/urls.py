from django.urls import path

from refugios import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('asociar_un_refugio/', views.asociar_un_refugio),
    path('adoptar_una_mascota/', views.adoptar_una_mascota),
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)