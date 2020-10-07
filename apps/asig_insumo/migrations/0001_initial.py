# Generated by Django 2.2.16 on 2020-09-15 03:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('periodo', '0001_initial'),
        ('insumo', '0001_initial'),
        ('zona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='asig_insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_asig', models.DateField(default=datetime.datetime.now)),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='periodo.periodo')),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='zona.zona')),
            ],
            options={
                'verbose_name_plural': 'asig_insumo',
                'verbose_name': 'asig_insumo',
                'db_table': 'asig_insumo',
            },
        ),
        migrations.CreateModel(
            name='detalle_asig_insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('asig_insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asig_insumo.asig_insumo')),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insumo.insumo')),
            ],
            options={
                'verbose_name_plural': 'detalles_asig_insumos',
                'verbose_name': 'detalle_asig_insumo',
                'db_table': 'detalle_asig_insumo',
            },
        ),
    ]
