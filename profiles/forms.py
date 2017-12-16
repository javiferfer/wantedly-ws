from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from profiles.models import Person

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=128, help_text="Please, introduce your username")
    password = forms.CharField(widget=forms.PasswordInput, max_length=128, help_text="Please, introduce your password")
    email = forms.CharField(widget=forms.TextInput, max_length=128, help_text="Please, introduce your email")

    class Meta:
        model = User
        # widgets = {'password': forms.PasswordInput(), 'name': forms.TextInput()}
        fields = ('username','password','email')


class PersonForm(forms.ModelForm):
    username = forms.CharField(max_length=128, help_text="Please, introduce your username")
    email = forms.CharField(widget=forms.TextInput, max_length=128, help_text="Please, introduce your email")
    name = forms.CharField(max_length=128, help_text="Please, introduce your name")
    age = forms.IntegerField(min_value=0, max_value=100, label='Age', error_messages={'min_value': 'You are too young', 'max_value': 'You are too old'})
    # sex = forms.CharField(widget=forms.TextInput, max_length=128, help_text="Male or Female")

    class Meta:
        model = Person
        # widgets = {'password': forms.PasswordInput(), 'name': forms.TextInput()}
        fields = ('username','email','name','age')