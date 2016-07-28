from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Ok now fuck off.")
