from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    html = loader.get_template('h/a3.html')
    return HttpResponse(html.render(request))
