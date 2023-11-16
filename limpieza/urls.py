from django.urls import path
from limpieza.views import proyecto, crear_limpieza, eliminar_limpieza, actualizar_limpieza, detalle_limpieza, limpiezas

urlpatterns = [
    path('', proyecto, name='proyecto'),
    path('limpiezas/', limpiezas, name='limpiezas'),
    path('crear/', crear_limpieza, name='crear_limpieza'),
    path('limpieza/<int:paleta_id>/', detalle_limpieza, name='detalle_limpieza'),
    path('limpieza/<int:paleta_id>/eliminar/', eliminar_limpieza, name='eliminar_limpieza'),
    path('limpieza/<int:paleta_id>/actualizar/', actualizar_limpieza, name='actualizar_limpieza'),
]
