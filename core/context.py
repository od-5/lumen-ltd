from .models import Setup, Contacts

__author__ = 'alexy'


def site_setup(request):
    try:
        qss = Setup.objects.all().first()
    except:
        qss = None
    try:
        qsc = Contacts.objects.all().first()
    except:
        qsc = None
    return {
        'setup': qss,
        'contacts': qsc,
    }
