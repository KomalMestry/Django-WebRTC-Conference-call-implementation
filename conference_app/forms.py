from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
  first_name = forms.CharField(label='first_name', max_length=100)
  email = forms.CharField(label='email', max_length=12, min_length=10)

  class Meta:
      model = User