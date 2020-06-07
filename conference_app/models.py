# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ConferenceRoom(models.Model):
    to_user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='to_user')
    from_user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='from_user')
    roomname = models.CharField(max_length=100, null=True)
    conference_name = models.CharField(max_length=100, null=True)
    is_accept = models.BooleanField(default=False)
    answer = models.BooleanField(default=False)
    organizer = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    starttime = models.TimeField(null=True)
    endtime = models.TimeField(null=True)

    class Meta:
        db_table = 'conference_room'
