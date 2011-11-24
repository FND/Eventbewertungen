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
         model=Event,
         template_name='events/detail.html')),
<<<<<<< HEAD
    (r'^(?P<event_id>\d+)/results/$', 'events.views.results'),
=======
    (r'^(?P<event_id>\d+)/talk/$', 'events.views.talk'),
>>>>>>> 9a5752a79be82c9d1e0ee9138171a0b5b021521d
)
