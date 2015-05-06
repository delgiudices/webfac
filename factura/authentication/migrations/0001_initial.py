# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('codigo', models.PositiveIntegerField()),
                ('username', models.CharField(unique=True, max_length=50)),
                ('sistema', models.ForeignKey(to='sistema.Sistema')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
