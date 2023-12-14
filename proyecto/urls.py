from django.urls import path
from proyecto.views import proyecto, aboutme, CrearDespensa, ModificarDespensa, DetalleDespensa, ListadoDespensas, EliminarDespensa

urlpatterns = [
    path('', proyecto, name='proyecto'),
    path('aboutme',aboutme , name='aboutme'),
    path('despensas/', ListadoDespensas.as_view(), name='despensas'),
    path('crear_despensa/', CrearDespensa.as_view(), name='crear_despensa'), 
    path('despensas/<int:pk>/', DetalleDespensa.as_view(), name='detalle_despensa'),
    path('proyecto/<int:pk>/modificar/', ModificarDespensa.as_view(), name='modificar_despensa'),
    path('proyecto/<int:pk>/eliminar/', EliminarDespensa.as_view(), name='eliminar_despensa')
]
