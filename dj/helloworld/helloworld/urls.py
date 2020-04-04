from django.conf.urls import url
from django.http import HttpResponse, FileResponse

def page(request):
    return HttpResponse("Hello World!")

def icon(request):
    return FileResponse(open('favicon.ico', 'rb'))

urlpatterns = [
    url(r'^favicon.ico$', icon),
    url(r'^', page),
]
