from django.shortcuts import render
from core.forms import TicketForm

__author__ = 'alexey'


def index(request):
    form = TicketForm()
    return render(request, 'index.html', {
        'form': form,
    })
