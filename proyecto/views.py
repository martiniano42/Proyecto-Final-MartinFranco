from django.shortcuts import render, redirect
from proyecto.models import Despensa
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


def proyecto(request):
    
    return render(request, 'proyecto/proyecto.html', {})

def aboutme(request):
    
    return render(request, 'proyecto/aboutme.html', {})

class ListadoDespensas(ListView):
    model = Despensa
    context_object_name = 'listado_de_despensas'
    template_name = 'proyecto/despensas.html'
    
    def get_queryset(self):
        nombre = self.request.GET.get('nombre')
        if nombre:
            listado_de_despensas = self.model.objects.filter(nombre__icontains=nombre)
        else:
            listado_de_despensas = self.model.objects.all()
        return listado_de_despensas



class DetalleDespensa(DetailView):
    model = Despensa
    template_name = "proyecto/detalle_despensa.html"
    
class CrearDespensa(LoginRequiredMixin, CreateView):
    model = Despensa
    template_name = "proyecto/crear_despensa.html"
    fields = ['nombre', 'apellido', 'biografia', 'fecha_creacion']
    success_url = reverse_lazy('despensas')

class ModificarDespensa(LoginRequiredMixin, UpdateView):
    model = Despensa
    template_name = "proyecto/modificar_despensa.html"
    fields = ['nombre','apellido', 'biografia', 'fecha_creacion']
    success_url = reverse_lazy('despensas')    

class EliminarDespensa(LoginRequiredMixin, DeleteView):
    model = Despensa
    template_name = "proyecto/eliminar_despensa.html"
    success_url = reverse_lazy('despensas')