# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exampleitem',
            name='list_images',
            field=models.ManyToManyField(blank=True, to='personal_site.ImageListField'),
        ),
    ]
