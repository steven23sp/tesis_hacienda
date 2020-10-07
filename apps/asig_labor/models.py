from datetime import datetime
from django.db import models
from django.forms import model_to_dict

from apps.labor.models import labor
from apps.periodo.models import periodo
from apps.empleado.models import empleado

estado = (
    (0, 'PENDIENTE'),
    (1, 'PAGADO')
)

class asig_labor(models.Model):
    fecha_asig = models.DateField(default=datetime.now)
    empleado = models.ForeignKey(empleado, on_delete=models.PROTECT)
    periodo = models.ForeignKey(periodo, on_delete=models.PROTECT)
    labor = models.ForeignKey(labor, on_delete=models.CASCADE)
    desde = models.DateField(default=datetime.now)
    hasta = models.DateField(default=datetime.now)
    total_dias = models.IntegerField(default=0)
    estado = models.IntegerField(choices=estado, default=0)
    valor_a_pag = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    saldo = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    valor_pag = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return '%s %s' % (self.fecha_asig, self.empleado.nombres)

    def toJSON(self):
        item = model_to_dict(self)
        item['empleado'] = self.trabajador.toJSON()
        item['labor'] = self.labor.toJSON()
        item['periodo'] = self.periodo.toJSON()
        item['estado'] = self.get_estado_display()
        return item

    class Meta:
        db_table = 'asig_labor'
        verbose_name = 'asig_labor'
        verbose_name_plural = 'asig_labor'
