from datetime import datetime
from django.db import models
from apps.empleado.models import empleado
from django.forms import model_to_dict

# Create your models here.
estado = (
    (0, 'ausente'),
    (1, 'asistio')
)


class asistencia(models.Model):
    fecha = models.DateField(default=datetime.now)
    estado = models.IntegerField(choices=estado)
    empleado = models.ForeignKey(empleado, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.empleado.nombres, self.fecha)

    def toJSON(self):
        item = model_to_dict(self)

    class Meta:
        db_table = 'asistencia'
        verbose_name = 'asistencia'
        verbose_name_plural = 'asistencias'
        ordering = ['-empleado', '-estado']




