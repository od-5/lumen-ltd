from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns
# from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'core.views.index', name='home'),
    url(r'^ticket/$', 'core.ajax.ticket_form', name='ticket'),
    url(r'^map/$', 'core.ajax.map', name='map'),
    # url(r'^address/$', 'apps.address.ajax.address_item_list', name='address'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^i18n/', include('django.conf.urls.i18n')),
)

urlpatterns += i18n_patterns(
    'core.views',
    url(r'^$', 'index', name='home'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
