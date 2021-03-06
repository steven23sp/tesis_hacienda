# Generated by Django 2.2.16 on 2020-09-15 03:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('periodo', '0001_initial'),
        ('zona', '0001_initial'),
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='produccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime.now)),
                ('cantidad', models.IntegerField(default=0)),
                ('perdida', models.IntegerField(default=0)),
                ('cantero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='zona.zona')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='periodo.periodo')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producto.producto')),
            ],
            options={
                'verbose_name_plural': 'producciones',
                'verbose_name': 'produccion',
                'db_table': 'produccion',
            },
        ),
    ]
