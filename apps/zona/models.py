from django.db import models
from django.forms import model_to_dict

area = (
    (1, 'METROS'),
    (0, 'HECTAREAS'),
)
estado = (
    (0, 'ACTIVO'),
    (1, 'INACTIVO')
)

SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


class zona(models.Model):
    nombre = models.CharField(max_length=50)
    dimesion = models.IntegerField(choices=area, default=1)
    valor_dim = models.FloatField(max_length=13)
    estado = models.IntegerField(choices=estado, default=1)

    def _area_total(self):
        if self.dimesion == 1:
            Area = self.valor_dim
            return Area
        else:
            Area = (self.valor_dim*1000)
            return Area
    area_total = property(_area_total)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return '%s %s %s %s' % (self.nombre, ' / ', self.area_total, '(m2)'.translate(SUP))

    class Meta:
        db_table = 'zona'
        verbose_name = 'zona'
        verbose_name_plural = 'zonas'
        ordering = ['-nombre', '-valor_dim']

