# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progApp', '0003_auto_20141122_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancerdata',
            name='stage',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
