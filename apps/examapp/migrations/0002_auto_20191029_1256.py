# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-29 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thought',
            name='users_who_like',
            field=models.ManyToManyField(related_name='liked_thoughts', to='examapp.User'),
        ),
    ]
