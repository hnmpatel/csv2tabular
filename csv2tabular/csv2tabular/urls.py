"""
Definition of urls for csv2tabular.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from django.conf.urls import include
from django.contrib import admin
from csv2tabular import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'app.views.home', name='home'),
    url(r'^upload/$', 'app.views.upload', name='upload'),
    url(r'^show-data/(?P<id>\d+)/$', 'app.views.view_data', name='show-data'),
    url(r'^show-db-data/(?P<id>\d+)/$', 'app.views.view_db_data', name='view_db_data'),

    url(r'^show_tabular_data/(?P<col1>\d+)/(?P<col2>\d+)/$', 'app.views.tabular_data', name='tabular_data'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)
