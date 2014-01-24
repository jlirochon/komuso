from django.conf.urls import patterns, include, url
from django.shortcuts import render
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'komuso.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),

    #url(r'^$', 'apps.core.views.home', name='home'),
    url(r'^', include('score-editor.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)

urlpatterns += staticfiles_urlpatterns()
