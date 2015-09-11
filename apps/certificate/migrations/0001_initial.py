# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'certificate/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f')),
                ('alt', models.CharField(max_length=500, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
            ],
            options={
                'verbose_name': '\u0421\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442',
                'verbose_name_plural': '\u0421\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u044b',
            },
            bases=(models.Model,),
        ),
    ]
