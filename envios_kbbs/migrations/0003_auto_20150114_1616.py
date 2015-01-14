# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envios_kbbs', '0002_auto_20150112_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='envio',
            name='fecha',
        ),
        migrations.AlterField(
            model_name='envio',
            name='fecha_envio',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
