# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LookUpData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(null=True, blank=True)),
                ('cancer', models.ForeignKey(to='progApp.Cancer')),
                ('gender', models.ForeignKey(blank=True, to='progApp.Gender', null=True)),
                ('stage', models.ForeignKey(blank=True, to='progApp.Stage', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cancerdata',
            name='years_lived',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='treatment',
            name='cost',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='treatment',
            name='quality_of_life',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cancer',
            name='type',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cancerdata',
            name='age',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cancerdata',
            name='gender',
            field=models.ForeignKey(blank=True, to='progApp.Gender', null=True),
            preserve_default=True,
        ),
    ]
