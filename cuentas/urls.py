from django.urls import path
from cuentas.views import login, registro, editar_perfil, CambiarPassword, detalle_perfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='cuentas/logout.html'), name='logout'),
    path('registro/', registro, name='registrarse'),
    path('editar/', editar_perfil, name='editar_perfil'),
    path('detalle/', detalle_perfil, name='detalle_perfil'),
    path('editar/password/', CambiarPassword.as_view(), name='cambiar_password')
]
