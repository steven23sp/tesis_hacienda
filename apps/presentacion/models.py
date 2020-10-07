from django.db import models
from django.forms import model_to_dict


# Create your models here.

class presentacion(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    abreviatura = models.CharField(max_length=10)

    def __str__(self):
        return '%s' % self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'presentacion'
        verbose_name = 'presentacion'
        verbose_name_plural = 'presentaciones'
        ordering = ['-nombre']
