from datetime import datetime
from django.db import models
from django.forms import model_to_dict

from apps.equipo_maquinaria.models import equipo_maquinaria
from apps.empleado.models import empleado

estado = (
    (0, 'Devuelto'),
    (1, 'Entregado')
)


class asig_eq_maq(models.Model):
    fecha_asig = models.DateField(default=datetime.now)
    empleado = models.ForeignKey(empleado, on_delete=models.PROTECT)
    equipo_maquinaria = models.ForeignKey(equipo_maquinaria, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.fecha_asig, self.empleado.nombres)

    def toJSON(self):
        item = model_to_dict(self)
        item['empleado'] = self.empleado.toJSON()
        item['equipo_maquinaria'] = self.equipo_maquinaria.toJSON()

        return item

    class Meta:
        db_table = 'asig_eq_maq'
        verbose_name = 'asig_eq_maq'
        verbose_name_plural = 'asig_equipos_maquinas'
