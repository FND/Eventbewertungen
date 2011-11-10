from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from events.models import Event
from talks.models import Talk

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
            queryset=Event.objects.order_by('-pub_date'),
            context_object_name='latest_events_list',
            template_name='events/index.html')),
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Talk,
            template_name='talks/detail.html')),
)
