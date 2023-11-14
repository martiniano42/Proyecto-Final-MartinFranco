from django.urls import path
from proyecto.views import proyecto, crear_bebida, crear_limpieza, despensas
from proyecto.views import Crear_Despensa

urlpatterns = [
    path('', proyecto, name='proyecto'),
    path('despensas/', despensas, name='despensas'),
    path('proyecto/crear_despensa/', Crear_Despensa.as_view(), name='crear_despensa'), 
    path('crear_bebida/', crear_bebida, name='crear_bebida'),
    path('crear_limpieza/', crear_limpieza, name='crear_limpieza')
]
