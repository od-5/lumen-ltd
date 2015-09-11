# coding=utf-8
import os
import uuid
from django.conf import settings
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize

__author__ = 'alexy'


class Certificate(models.Model):
    class Meta:
        verbose_name = u"Сертификат"
        verbose_name_plural = u"Сертификаты"
        app_label = 'certificate'

    def __unicode__(self):
        if self.alt:
            return self.alt
        else:
            return self.image.url

    image = models.ImageField(verbose_name=u'Изображения', upload_to='certificate/')
    image_resize = ImageSpecField(
        [SmartResize(*settings.CERTIFICATE_SIZE)], source='image', format='JPEG', options={'quality': 94}
    )
    alt = models.CharField(verbose_name=u'Описание', max_length=500, null=True, blank=True)

