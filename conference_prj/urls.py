"""conference_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from conference_app.views import demo, audio, audio_video, HomeView, user_register, auth_login, auth_logout, \
    profile, exitcall, join, room,connect,multiple_video

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^conference/', demo),
    url(r'^home/', HomeView.as_view(), name="home"),
    url(r'^audio/', audio, name="audio"),
    url(r'^audio-video/', audio_video, name="audio-video"),
    url(r'^register/$', user_register, name='user_register'),
    url(r'login/$', auth_login, name='login'),
    url(r'profile/$', profile, name='profile'),
    url('signout', auth_logout, name='logout'),
    url('room/(?P<name>.+)', room, name='room'),
    url('join', join, name='join'),
    url('exit/', exitcall, name='exit'),
    url(r'connect/$', connect, name='connect'),
    url(r'multiple_video/$', multiple_video, name='multiple_video'),
]
