from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Story


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('parent', 'content', 'writer')