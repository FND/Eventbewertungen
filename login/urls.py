from django.conf.urls.defaults import *

urlpatterns = patterns('',
(r'^$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
)
