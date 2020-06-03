# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView, FormView
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet

from conference_app.forms import UserForm


def demo(request):
    return render(request, 'index.html')


def audio(request):
    return render(request, 'audio.html')


def audio_video(request):
    return render(request, 'audio_video.html')


# @api_view(['POST'])
class HomeView(FormView):
    def get(self,request):
        form=UserForm()
        return render(request,'home.html',{'form':form})

    def post(self,request):
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
