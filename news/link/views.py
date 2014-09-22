from django.http import HttpResponse

def hello_world(request):
    message = 'Hey, this is my first view!'
    return HttpResponse(message)
