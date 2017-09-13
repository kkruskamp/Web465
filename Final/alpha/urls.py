from django.conf.urls import url
from .models import *
from . import views

urlpatterns = [
    url(r'^$', views.Index),
    url(r'^login/$', views.Login, name='login'),
    url(r'^logout/$', views.Logout, name='logout'),
    url(r'^register/$', views.Register, name='register'),
    url(r'^index/$', views.Index, name='Index'),
    url(r'^home/$', views.Home, name='home'),
    url(r'^post/$', views.Post, name='post'),
    url(r'^messages/$', views.Messages, name='messages'),
]
