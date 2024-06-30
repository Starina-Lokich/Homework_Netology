import datetime
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello from Django')

def time(request):
    current_time = datetime.datetime.now().time()
    return HttpResponse(f'Time = {current_time}')