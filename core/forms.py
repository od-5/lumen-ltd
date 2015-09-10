from django.forms import ModelForm
from core.models import Ticket

__author__ = 'alexy'


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('name', 'phone', 'email')