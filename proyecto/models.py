from django.db import models
from ckeditor.fields import RichTextField

class Despensa(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    biografia = RichTextField()
    fecha_creacion = models.DateField()
    
    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.apellido} - {self.fecha_creacion}'