# coding=utf-8
from django.contrib import admin
from .models import Certificate


class CertificateAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'preview']

    def preview(self, img):
        return "<img src='%s'/>" % img.image_resize.url

    preview.short_description = u"Превью"
    preview.allow_tags = True

admin.site.register(Certificate, CertificateAdmin)