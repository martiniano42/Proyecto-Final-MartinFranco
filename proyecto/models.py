from django.db import models
from ckeditor.fields import RichTextField

class Despensa(models.Model):
    nombre = models.CharField(max_length=30)
    biografia = RichTextField()
    year = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.year}'
    
class Bebidas(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    
class Limpieza(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField()
    cantidad = models.IntegerField()