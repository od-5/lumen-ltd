# coding=utf-8
from annoying.decorators import ajax_request
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from core.forms import TicketForm
from .models import Setup, City

__author__ = 'alexy'


@csrf_exempt
@ajax_request
def ticket_form(request):
    try:
        email = Setup.objects.all()[0].email
    except:
        email = 'od-5@yandex.ru'
    print email
    if request.method == "POST":
        form = TicketForm(data=request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.status = 1
            ticket.save()
            message = u'Имя: %s\nТелефон:%s\nE-mail: %s\n' % (ticket.name, ticket.phone, ticket.phone)
            print settings.EMAIL_HOST_USER
            send_mail(
                u'lumen-ltd.com - Заявка с сайта',
                message,
                settings.EMAIL_HOST_USER,
                [email, ]
            )
            return {
                'success': True
            }
        else:
            return {
                'success': False
            }
    return {
        'success': False
    }


@ajax_request
def map(request):
    request.encoding = 'utf-8'
    if request.is_ajax():
        query = City.objects.all()
        result = []
        for item in query:
            result_json = {}
            result_json['name'] = item.name
            result_json['coord_x'] = float(item.coord_x)
            result_json['coord_y'] = float(item.coord_y)
            result.append(result_json)
        data = result
    else:
        data = {'msg': 'fail'}
    return data
