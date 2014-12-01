# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progApp', '0005_auto_20141130_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalTrial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stage', models.PositiveIntegerField(null=True, blank=True)),
                ('age_hi', models.PositiveIntegerField(null=True, blank=True)),
                ('age_low', models.PositiveIntegerField(null=True, blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('contact_info', models.CharField(max_length=400, null=True, blank=True)),
                ('location', models.CharField(max_length=100, null=True, blank=True)),
                ('cancer', models.ForeignKey(to='progApp.Cancer')),
                ('gender', models.ForeignKey(blank=True, to='progApp.Gender', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
