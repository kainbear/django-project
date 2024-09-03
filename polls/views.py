from django.http import HttpResponse


def index(request):
    return HttpResponse("Что пацаны джанго да?")