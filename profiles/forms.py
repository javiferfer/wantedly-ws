from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=128, help_text="Please, introduce your username")
    password = forms.CharField(widget=forms.PasswordInput, max_length=128, help_text="Please, introduce your password")
    class Meta:
        model = User
        widgets = {'password': forms.PasswordInput()}
        fields = ('username','password')
