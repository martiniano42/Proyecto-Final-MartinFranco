from django.db import models
from ckeditor.fields import RichTextField

class Limpieza(models.Model):
    producto = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    descripcion = RichTextField()
    vencimiento = models.DateField()
    avatar = models.ImageField(upload_to='avatares2', null=True, blank=True)
    
    def __str__(self):
        return f'{self.producto} - {self.marca} - {self.vencimiento}'