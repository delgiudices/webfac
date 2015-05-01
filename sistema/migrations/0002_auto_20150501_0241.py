# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sistemamodel',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='sistemamodel',
            name='sistema',
        ),
        migrations.DeleteModel(
            name='SistemaModel',
        ),
    ]
