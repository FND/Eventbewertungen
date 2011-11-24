# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from events.models import Event
<<<<<<< HEAD
import datetime
from django.http import HttpResponse
=======
>>>>>>> 9a5752a79be82c9d1e0ee9138171a0b5b021521d

@login_required
def detail(request, event_id):
    p = get_object_or_404(Event, pk=event_id)
    raise Exception("bla")
    return render_to_response('events/detail.html', {'event': p},
                               context_instance=RequestContext(request))
<<<<<<< HEAD

def talk(request):
    pass

def results(request, event_id):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
=======
>>>>>>> 9a5752a79be82c9d1e0ee9138171a0b5b021521d
