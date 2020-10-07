from django.db import models
from django.forms import model_to_dict

from apps.categoria.models import categoria
from apps.presentacion.models import presentacion


class producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(categoria, on_delete=models.PROTECT, null=True, blank=True)
    presentacion = models.ForeignKey(presentacion, on_delete=models.PROTECT, null=True, blank=True)
    descripcion = models.CharField(max_length=100)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s %s' % (self.nombre, ' / ', self.presentacion.nombre)

    def toJSON(self):
        item = model_to_dict(self)
        item['categoria'] = self.categoria.toJSON()
        item['presentacion'] = self.presentacion.toJSON()
        item['pvp'] = format(self.pvp, '.2f')
        return item

    class Meta:
        db_table = 'producto'
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['-id']

