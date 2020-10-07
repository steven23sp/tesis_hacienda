from django.db import models
from django.forms import model_to_dict


# Create your models here.
class labor(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30 , null=True, blank=True )
    valor_dia = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return '%s %s %s %s' % (self.nombre, '/', '$', self.valor_dia)

    def toJson(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'labor'
        verbose_name = 'labor'
        verbose_name_plural = 'labores'
        ordering = ['id', 'nombre']
