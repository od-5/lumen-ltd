# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_ticket_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='email',
            field=models.EmailField(default='', max_length=256, verbose_name='e-mail'),
            preserve_default=False,
        ),
    ]
