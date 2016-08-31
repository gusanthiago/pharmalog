# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='cod_barra',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='medicamento_entrada',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicamento_saida',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]
