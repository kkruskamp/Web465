from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from chat_app import settings
from .models import Chat
from django.contrib.auth.models import User
from .forms import *
# from django.core.context_processors import csrf
# from models import MyRegistrationForm

def Index(request):
    return render(request,'alpha/index.html')

def Login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Account is not active at the moment.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, "alpha/login.html", {'next': next})

#########################################################################################################
def Register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    context = {
        'title':'Register',
        'form':form,
    }

    return render(request, 'alpha/register.html', context)
#########################################################################################################

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/index/')

def Home(request):
    c = Chat.objects.all()
    return render(request, "alpha/home.html", {'home': 'active', 'chat': c})

#View sends it back to javascript if valid as a JsonResponse
def Post(request):
    if request.method == "POST":
        #captured data is pushed into new chat instance
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message=msg)
        #as long as data isnt empty, save it to database
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')

def Messages(request):
    c = Chat.objects.all()
    return render(request, 'alpha/messages.html', {'chat': c})
