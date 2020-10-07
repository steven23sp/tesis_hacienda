from datetime import date
from django.db import models
from django.forms import model_to_dict

opcion = (
    (0, 'equipo'),
    (1, 'herramienta')
)
# Create your models here.

class equipo_maquinaria(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.IntegerField(choices=opcion)
    descripcion = models.CharField(max_length=30)
    fecha_registro = models.DateField(default=date.today)

    def __str__(self):
        return '%s' % self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'equipo_maquinaria'
        verbose_name = 'equipo_maquinaria'
        verbose_name_plural = 'equipo_maquinarias'
        ordering = ['-nombre', '-tipo', '-fecha_registro']
