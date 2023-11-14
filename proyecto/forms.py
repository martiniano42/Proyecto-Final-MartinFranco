from django import forms

    
class BusquedaDespensaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
    
class CrearBebidasFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    cantidad = forms.IntegerField()
    
class CrearLimpiezaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    cantidad = forms.IntegerField()