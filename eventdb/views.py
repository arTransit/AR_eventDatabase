import json
from django.http import HttpResponse, HttpRequest
from django.template import RequestContext, loader
from eventdb.models import Event

def index(request):
    event_list = Event.objects.order_by('-event_date')

    if 'application/json' in request.META['HTTP_ACCEPT']:
        return HttpResponse(
                json.dumps( [e.to_DICT() for e in event_list] ),
                "application/json" )
    else:
        template = loader.get_template('eventdb/index.html')
        context = RequestContext(request, {'event_list':event_list,})
        return HttpResponse(template.render(context))


def detail(request, event_id):
    return HttpResponse("Detail of : %s" % event_id)


