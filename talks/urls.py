from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from talks.models import Talk
from polls.models import Poll

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
            queryset=Talk.objects.order_by('-pub_date'),
            context_object_name='latest_vortrag_list',
            template_name='talk/index.html')),
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name='poll/detail.html')),
        )
