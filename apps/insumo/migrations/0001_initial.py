# Generated by Django 2.2.16 on 2020-09-15 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('presentacion', '0001_initial'),
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('pvp', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9, null=True)),
                ('stock', models.IntegerField(blank=True, default=0, null=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='categoria.categoria')),
                ('presentacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='presentacion.presentacion')),
            ],
            options={
                'verbose_name_plural': 'insumos',
                'db_table': 'insumo',
                'ordering': ['id', 'nombre'],
                'verbose_name': 'insumo',
            },
        ),
    ]
