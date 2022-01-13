from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms import widgets
# from django.forms.models import _Labels
from django.forms.widgets import DateInput, EmailInput, PasswordInput, TextInput

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
