# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='SistemaModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.PositiveIntegerField()),
                ('sistema', models.ForeignKey(to='sistema.Sistema')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='sistemamodel',
            unique_together=set([('codigo', 'sistema')]),
        ),
    ]
