from django.http import HttpResponse
from django.template import RequestContext, loader
from eventdb.models import Event

def index(request):
    event_list = Event.objects.order_by('-event_date')
    template = loader.get_template('eventdb/index.html')
    context = RequestContext(request, {'event_list':event_list,})
    return HttpResponse(template.render(context))


def detail(request, event_id):
    return HttpResponse("Detail of : %s" % event_id)


