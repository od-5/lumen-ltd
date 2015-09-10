# coding=utf-8
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_tpd9(a+n4i20i$5j6$cw^%09q=i6_r1e-j8ur-e@uw91#g@hd'

YANDEX_MAPS_API_KEY = 'AO7kF1UBAAAA-akFCwIAR7_VYsSjwJ9g-dDEVHElLxuBQi8AAAAAAAAAAAAQMK4N7NYtvg4ALgMZ8-GRO_cQqQ=='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

if DEBUG:
    EMAIL_HOST = 'smtp.yandex.ru'
    EMAIL_HOST_USER = 'od-5@yandex.ru'
    EMAIL_HOST_PASSWORD = 'gladiator1'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    DEFAULT_FROM_EMAIL = 'admin@lumen-ltd.com'
    EMAIL_HOST = 'smtp.fullspace.ru'
    EMAIL_HOST_USER = 'admin@lumen-ltd.com'
    EMAIL_HOST_PASSWORD = 'alena2010'

# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'widget_tweaks',
    'annoying',
    'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'core.context.site_setup',
)

INTERNAL_IPS = '127.0.0.1'
ROOT_URLCONF = 'landing.urls'

WSGI_APPLICATION = 'landing.wsgi.application'

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'enjoyafrru_lumen',
             'USER': 'enjoyafrru_lumen',
             'PASSWORD': 'f3ccb431',
             'HOST': 'localhost',
             'PORT': '',
         }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': u'Landing',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        'sites',
        # {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
        {'label': u'Настройки', 'icon': 'icon-cog', 'models': ('auth.user', 'auth.group', 'core.setup')},
        {'label': u'Контакты', 'icon': 'icon-cog', 'models': ('core.contacts',)},
        {'label': u'Заявки', 'icon': 'icon-user', 'models': ('core.ticket',)},
        {'label': u'Города', 'models': ('core.city',)},
    ),
}
