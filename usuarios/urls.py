from django.urls import path

from usuarios import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('subi_tu_post/', views.subi_tu_post),
    path('login/', views.login_view, name="login"),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('reset_password/', views.reset_password),
    path('main_login/', views.main_login),
    path('change_password/', views.change_password),
    path('mi_busqueda/', views.mi_busqueda),
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)