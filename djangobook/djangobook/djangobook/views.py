from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Welcome to the Home Page View!")

def hello(request):
    return HttpResponse("Hello World!")

