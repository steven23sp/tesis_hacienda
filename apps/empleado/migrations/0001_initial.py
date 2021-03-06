# Generated by Django 2.2.16 on 2020-09-15 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=10)),
                ('correo', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(max_length=10, unique=True)),
                ('direccion', models.CharField(max_length=50)),
                ('estado_civil', models.IntegerField(choices=[(0, 'casado'), (1, 'soltero')])),
                ('educ_primaria', models.CharField(max_length=50)),
                ('educ_secundaria', models.CharField(max_length=50)),
                ('educ_superior', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'empleados',
                'db_table': 'empleado',
                'ordering': ['-nombres', '-cedula', '-apellidos'],
                'verbose_name': 'empleado',
            },
        ),
    ]
