from django.shortcuts import render
from apps.certificate.models import Certificate
from core.forms import TicketForm

__author__ = 'alexey'


def index(request):
    form = TicketForm()
    certificate_list = Certificate.objects.all()
    return render(request, 'index.html', {
        'form': form,
        'certificate_list': certificate_list,
    })
