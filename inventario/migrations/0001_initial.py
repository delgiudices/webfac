# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ajuste',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('costo', models.DecimalField(max_digits=6, decimal_places=2)),
                ('precio', models.DecimalField(max_digits=6, decimal_places=2)),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('sistema', models.ForeignKey(to='sistema.Sistema')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ajuste',
            name='articulo',
            field=models.ForeignKey(to='inventario.Articulo'),
        ),
        migrations.AlterUniqueTogether(
            name='articulo',
            unique_together=set([('codigo', 'sistema')]),
        ),
    ]
