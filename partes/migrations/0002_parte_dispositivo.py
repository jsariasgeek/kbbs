# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parte',
            name='dispositivo',
            field=models.CharField(default='Sin descripcion', max_length=120),
            preserve_default=False,
        ),
    ]
