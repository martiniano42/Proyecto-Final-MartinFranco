from django.shortcuts import render, redirect
from limpieza.models import Limpieza
from limpieza.forms import CrearLimpiezaFormulario, BusquedaLimpiezaFormulario, ActualizarLimpiezaFormulario
from django.contrib.auth.decorators import login_required


def proyecto(request):
    
    return render(request, 'proyecto/proyecto.html', {})

def limpiezas(request):
    formulario = BusquedaLimpiezaFormulario(request.GET)
    if formulario.is_valid():
        producto_a_buscar = formulario.cleaned_data.get('producto')
        listado_de_limpieza = Limpieza.objects.filter(producto__icontains=producto_a_buscar)
    
    formulario = BusquedaLimpiezaFormulario()
    return render(request, 'limpieza/limpiezas.html', {'formulario': formulario, 'listado_de_limpieza': listado_de_limpieza})


@login_required
def crear_limpieza(request):
    if request.method == 'POST':
        formulario = CrearLimpiezaFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            producto = info_limpia.get('producto')
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            vencimiento = info_limpia.get('vencimiento')
            avatar = info_limpia.get('avatar')
    
            limpieza = Limpieza(producto=producto, marca=marca.lower(), descripcion=descripcion, vencimiento=vencimiento, avatar=avatar)
            limpieza.save()
            
            return redirect('limpiezas')
        else:
            return render(request, 'limpieza/limpieza.html', {'formulario': formulario})
        
    formulario = CrearLimpiezaFormulario()
    return render(request, 'limpieza/crear_limpieza.html', {'formulario': formulario})

@login_required
def eliminar_limpieza(request, limpieza_id):
    limpieza_a_eliminar = Limpieza.objects.get(id=limpieza_id)
    limpieza_a_eliminar.delete()
    return redirect("limpiezas")

@login_required
def actualizar_limpieza(request, limpieza_id):
    limpieza_a_actualizar = Limpieza.objects.get(id=limpieza_id)

    if request.method == "POST":
        formulario = ActualizarLimpiezaFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            limpieza_a_actualizar.producto = info_nueva.get('producto')
            limpieza_a_actualizar.marca = info_nueva.get('marca')            
            limpieza_a_actualizar.descripcion = info_nueva.get('descripcion')
            limpieza_a_actualizar.vencimiento = info_nueva.get('vencimiento')
            limpieza_a_actualizar.avatar = info_nueva.get('avatar')
            
            limpieza_a_actualizar.save()
            return redirect('limpiezas')
        else:
            return render(request, 'limpieza/actualizar_limpieza.html', {'formulario': formulario})
 
 
 
    formulario = ActualizarLimpiezaFormulario(initial={'producto': limpieza_a_actualizar.producto, 'marca': limpieza_a_actualizar.marca, 'descripcion': limpieza_a_actualizar.descripcion, 'vencimiento': limpieza_a_actualizar.vencimiento, 'avatar': limpieza_a_actualizar.avatar})
    return render(request, 'limpieza/actualizar_limpieza.html', {'formulario': formulario})

def detalle_limpieza(request, limpieza_id):
    limpieza = Limpieza.objects.get(id=limpieza_id)
    return render(request, 'limpieza/detalle_limpieza.html', {'limpieza': limpieza})
