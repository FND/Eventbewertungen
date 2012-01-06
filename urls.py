from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    (r'^polls/', include('polls.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/', include('login.urls')),
    (r'^talks/', include('talks.urls')),
    (r'^events/', include('events.urls')),
)
