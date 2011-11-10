from django.conf.urls.defaults import *
from django.views.generic import ListView
from events.models import Event

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
            queryset=Event.objects.order_by('-pub_date'),
            context_object_name='latest_events_list',
            template_name='events/index.html')),
)
