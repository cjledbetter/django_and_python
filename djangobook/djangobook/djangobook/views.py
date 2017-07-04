from django.http import HttpResponse

import datetime

def homepage(request):
    return HttpResponse("Welcome to the Home Page View!")

def hello(request):
    return HttpResponse("Hello World!")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be  %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
                        
