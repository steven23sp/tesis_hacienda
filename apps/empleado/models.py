from datetime import datetime
from django.db import models
from django.forms import model_to_dict


# Create your models here.
estado_civil = (
    (0, 'Casad@'),
    (1, 'Solter@')
)

estado = (
    (0, 'Activo '),
    (1, 'Inactivo')
)

class empleado(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10)
    edad = models.IntegerField(default=0)
    correo = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=50)
    estado_civil = models.IntegerField(choices=estado_civil, default=0)
    fecha_nac = models.DateField()
    estado = models.IntegerField(choices=estado, default= 0)
    educ_primaria = models.CharField(max_length=50)
    educ_secundaria = models.CharField(max_length=50)
    educ_superior = models.CharField(max_length=50)


    def __str__(self):
        return '%s %s ' % (self.nombres, self.apellidos)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'empleado'
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'
        ordering = ['-nombres', '-cedula', '-apellidos']
