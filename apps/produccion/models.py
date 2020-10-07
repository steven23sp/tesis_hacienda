from datetime import datetime
from django.db import models
from django.forms import model_to_dict

from apps.zona.models import zona
from apps.labor.models import labor
from apps.periodo.models import periodo
from apps.presentacion.models import presentacion
from apps.producto.models import producto
from apps.empleado.models import empleado


class produccion(models.Model):
    fecha = models.DateField(default=datetime.now)
    periodo = models.ForeignKey(periodo, on_delete=models.PROTECT)
    cantero = models.ForeignKey(zona, on_delete=models.PROTECT)
    producto = models.ForeignKey(producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField(default=0)
    perdida = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s' % (self.fecha, self.cantero.nombre)

    def toJSON(self):
        item = model_to_dict(self)
        item['cantero'] = self.cantero.toJSON()
        item['periodo'] = self.periodo.toJSON()
        item['producto'] = self.producto.toJSON()
        return item

    class Meta:
        db_table = 'produccion'
        verbose_name = 'produccion'
        verbose_name_plural = 'producciones'