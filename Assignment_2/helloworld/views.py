from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    html = "<html><body> CINS465 Hello World </body></html>"
    return HttpResponse(html)
