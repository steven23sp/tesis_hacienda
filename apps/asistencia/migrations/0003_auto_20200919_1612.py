# Generated by Django 2.2.16 on 2020-09-19 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0002_asistencia_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
