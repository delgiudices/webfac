# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0002_auto_20150501_0040'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sistema',
        ),
    ]
