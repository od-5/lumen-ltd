# coding=utf-8
from django.contrib import admin
from .models import Ticket, Setup, Contacts, City
from django.forms import ModelForm
from suit.widgets import EnclosedInput, AutosizedTextarea

__author__ = 'alexey'


class TicketAdminForm(ModelForm):
    class Meta:
        widgets = {
            'comment': AutosizedTextarea,
            'ticket_comment': AutosizedTextarea,
        }


class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created', 'status', 'comment')
    list_filter = ['created', 'status']
    date_hierarchy = 'created'
    form = TicketAdminForm

    def suit_row_attributes(self, obj, request):
        css_class = {
            1: 'success',
            0: 'warning',
            2: 'error',
        }.get(obj.status)
        if css_class:
            return {'class': css_class, 'data': obj.name}

class SetupAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'email')


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address')

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Setup, SetupAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(City)
