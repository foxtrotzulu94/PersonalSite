# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_site', '0006_award_honor_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='exampleitem',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='experienceitem',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='gametitle',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='imagelistfield',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='personalinterest',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='personalproject',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]