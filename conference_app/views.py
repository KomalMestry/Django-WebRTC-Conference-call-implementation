# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView, FormView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.viewsets import ViewSet
from datetime import datetime
from conference_app.forms import UserForm
from conference_app.models import ConferenceRoom


def demo(request):
    return render(request, 'index.html')


@login_required
def audio(request, *args):
    return render(request, 'audio.html')


@login_required
def room(request, name=None, organizer=None):
    host = request.get_host()
    user = request.user
    conference_name = "http://" + host + "/room/" + name
    from_user = User.objects.filter(email__icontains=name)
    try:
        if user == from_user:
            organizer = True
    except:
        organizer = False

    room = ConferenceRoom.objects.update_or_create(to_user_id=user.id, from_user_id=from_user[0].id,
                                                   defaults={
                                                            "to_user_id":user.id,
                                                            "from_user_id":from_user[0].id,
                                                            "roomname":name,
                                                            "conference_name":conference_name,
                                                            "organizer":organizer
                                                            })
    return render(request, 'audio.html')

@login_required
def audio_video(request):
    return render(request, 'audio_video.html')

@login_required
def profile(request):
    useremail = request.user.email.split('@')[0]
    print("***************************", useremail)
    return render(request, 'profile.html', {"context": useremail})

@login_required
def join(request):
    return render(request, 'join.html')

@login_required
def connect(request):
    user = request.user
    is_accept = ConferenceRoom.objects.filter(to_user=user, is_accept=True)
    conference_name=is_accept[0].conference_name
    if is_accept and conference_name:
        print("$$$$$$$$$$$$$$$$")
        return redirect(conference_name)
    else:
        print("&&&&&&&&&&&&&")
        messages.error(request, 'Something went wrong !!')
        return render(request, 'join.html', {
                    'error_message': 'Something went wrong !!'
                })


# def exitcall(request, roomname=None):
#     user = request.user
#     users = ConferenceRoom.objects.filter(roomname=roomname)
#     currentdate = datetime.today().time()
#     endtime = ConferenceRoom.objects.filter(to_user=user.id).update(endtime=currentdate)
#     return render(request, 'exit.html', {"context": users})

@login_required
def exitcall(request):
    return render(request, 'exit.html')

@login_required
def multiple_video(request):
    return render(request, 'multiple_video.html')

# @api_view(['POST'])
class HomeView(FormView):
    def get(self, request):
        form = UserForm()
        return render(request, 'home.html', {'form': form})

    def post(self, request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = UserForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # import ipdb;
                # ipdb.set_trace()
                # process the data in form.cleaned_data as required
                p = form.save()
                name = form.cleaned_data['name']
                email = form.cleaned_date['email']
                p = User(first_name=name, email=email)
                p.save()
                # redirect to a new URL:
                # return HttpResponseRedirect('/success/')
                return redirect('audio')
        # if a GET (or any other method) we'll create a blank form
        else:
            form = UserForm()

        return render(request, 'home.html', {'form': form})


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'home.html'
    # import ipdb;ipdb.set_trace()
    if request.method == 'POST':
        user = User()
        user.username = request.POST['username'] if request.POST.get('username') else None
        user.first_name = request.POST['first_name'] if request.POST.get('first_name') else None
        user.last_name = request.POST['last_name'] if request.POST.get('last_name') else None
        user.email = request.POST['email'] if request.POST.get('email') else None
        user.password = request.POST['password'] if request.POST.get('password') else None
        # import ipdb;ipdb.set_trace()
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            # elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
            #     return render(request, template, {
            #         'form': form,
            #         'error_message': 'Passwords do not match.'
            #     })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()

                # Login the user
                login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect('login')

    # No post data availabe, let's just show the page.
    else:
        form = UserForm()

    return render(request, template, {'form': form})


def auth_login(request):
    try:
        context = {}
        if request.method == 'POST':
            username = request.POST['username'].strip()
            password = request.POST['password'].strip()
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('profile'))
            else:
                # messages.error(request, 'Provide valid credentials!!')
                return HttpResponseRedirect('home')

        return render(request, "login.html", context)
    except Exception as e:
        return HttpResponseRedirect(reverse('login'))

@login_required
def auth_logout(request):
    if request.user:
        logout(request)

    return HttpResponseRedirect(reverse('login'))
