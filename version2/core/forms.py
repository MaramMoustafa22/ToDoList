from dataclasses import field
import imp
from turtle import title
from django import forms
from django.forms import ModelForm

from .models import *


class TodoForm(forms.ModelForm):

    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'What do you want to do!'}))
    class Meta:
        model = Todo

        fields = '__all__'



