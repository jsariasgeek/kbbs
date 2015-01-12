# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('responsables_dhl', '0001_initial'),
        ('partes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now=True)),
                ('sro', models.BigIntegerField(max_length=60)),
                ('fecha_envio', models.DateField(auto_now=True)),
                ('waybill', models.BigIntegerField()),
                ('picture', models.ImageField(upload_to=b'kbbs')),
                ('parte', models.ForeignKey(to='partes.Parte')),
                ('responsable_dhl', models.ForeignKey(to='responsables_dhl.Mensajero')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
