# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 06:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal_site', '0002_exampleitem_list_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtracurricularExperience',
            fields=[
                ('workexperience_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='personal_site.WorkExperience')),
            ],
            options={
                'abstract': False,
            },
            bases=('personal_site.workexperience',),
        ),
        migrations.CreateModel(
            name='VolunteerExperience',
            fields=[
                ('workexperience_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='personal_site.WorkExperience')),
                ('ext_url', models.URLField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('personal_site.workexperience',),
        ),
        migrations.RenameModel(
            old_name='CommercialGames',
            new_name='GameTitle',
        ),
        migrations.RenameModel(
            old_name='Hobbies',
            new_name='PersonalInterest',
        ),
        migrations.RenameModel(
            old_name='Projects',
            new_name='PersonalProject',
        ),
    ]
