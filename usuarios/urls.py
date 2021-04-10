from django.urls import path

from usuarios import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import login, logout
from django.urls import path, include
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('subi_tu_post/', login_required(views.subi_tu_post)),
    path('login/', views.login_view, name="login"),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('reset_password/', views.reset_password),
    path('main_login/', login_required(views.main_login)),
    path('change_password/', views.change_password),
    path('mi_busqueda/', login_required(views.mi_busqueda)),
    path('busquedas/', views.busquedas),

]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)