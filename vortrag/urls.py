from django.conf.urls.defaults import *
from django.views.generic import ListView
from polls.models import Vortrag

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
            queryset=Vortrag.objects.order_by('-pub_date'),
            context_object_name='latest_vortrag_list',
            template_name='vortrag/index.html')),
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Vortrag,
            template_name='vortrag/detail.html')),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Vortrag,
            template_name='vortrag/results.html'),
        name='vortrag_results'),
        )
