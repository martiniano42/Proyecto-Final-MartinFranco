from django.shortcuts import render, redirect
from proyecto.models import Despensa, Bebidas, Limpieza
from proyecto.forms import BusquedaDespensaFormulario, CrearBebidasFormulario
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def proyecto(request):
    
    return render(request, 'proyecto/proyecto.html', {})

def despensas(request):

    formulario = BusquedaDespensaFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre')
        listado_de_despensas = Despensa.objects.filter(nombre__icontains=nombre_a_buscar)
    
    formulario = BusquedaDespensaFormulario()
    return render(request, 'proyecto/despensas.html', {'formulario': formulario, 'listado_de_despensas': listado_de_despensas})


class Crear_Despensa(LoginRequiredMixin, CreateView):
    model = Despensa
    template_name = "proyecto/despensas.html"
    fields = ['nombre', 'biografia', 'year']
    success_url = reverse_lazy('despensas')



def crear_bebida(request):
    if request.method == 'POST':
        formulario = CrearBebidasFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            cantidad = info_limpia.get('cantidad')
    
            bebida = Bebidas(marca=marca.lower(), descripcion=descripcion, cantidad=cantidad)
            bebida.save()
            
            return redirect('despensas')
        else:
            return render(request, 'proyecto/crear_bebida.html', {'formulario': formulario})
        
    formulario = CrearBebidasFormulario()
    return render(request, 'proyecto/crear_bebida.html', {'formulario': formulario})

def crear_limpieza(request):
    if request.method == 'POST':
        formulario = CrearBebidasFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            cantidad = info_limpia.get('cantidad')
    
            limpieza = Limpieza(marca=marca.lower(), descripcion=descripcion, cantidad=cantidad)
            limpieza.save()
            
            return redirect('despensas')
        else:
            return render(request, 'proyecto/crear_limpieza.html', {'formulario': formulario})
        
    formulario = CrearBebidasFormulario()
    return render(request, 'proyecto/crear_limpieza.html', {'formulario': formulario})