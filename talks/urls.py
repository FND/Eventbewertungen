from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from talks.models import Talk
from polls.models import Poll

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
            queryset=Talk.objects.order_by('-pub_date'),
            context_object_name='latest_talk_list',
            template_name='talks/index.html')),
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Talk,
            template_name='talks/detail.html')),
        )
