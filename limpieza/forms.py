from django import forms
from ckeditor.fields import RichTextFormField


# otrea version de formulario de paleta
# class PaletaFormulario(forms.Form):
#     class Meta:
#         model = Paleta
#         fields = ['marca', 'descripcion', 'anio']
        

class BaseLimpiezaFormulario(forms.Form):
    producto = forms.CharField(max_length=30)
    marca = forms.CharField(max_length=30)
    descripcion = RichTextFormField()
    vencimiento = forms.DateField()
    avatar = forms.ImageField(required=False)
    
    

class CrearLimpiezaFormulario(BaseLimpiezaFormulario):
    ...


class ActualizarLimpiezaFormulario(BaseLimpiezaFormulario):
    ...
    
class BusquedaLimpiezaFormulario(forms.Form):
    producto = forms.CharField(max_length=30, required=False)
    