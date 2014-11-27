# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progApp', '0002_auto_20141120_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='quickcancerlookup',
            name='cancer',
            field=models.ForeignKey(blank=True, to='progApp.Cancer', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lookupdata',
            name='stage',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
