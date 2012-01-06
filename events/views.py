# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from events.models import Event
from talks.models import Talk
import datetime
from django.http import HttpResponse


@login_required
def detail(request, event_id):
    p = get_object_or_404(Event, pk=event_id)
    raise Exception("bla")
    return render_to_response('events/detail.html', {'event': p},
                               context_instance=RequestContext(request))


def talk(request):
    pass


def results(request, event_id):
    p = get_object_or_404(Event, pk=event_id)
    return render_to_response('events/results.html', {'event': p},
                               context_instance=RequestContext(request))
