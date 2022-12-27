from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField()
    address = forms.CharField()

    class Meta:
        model= User
        fields =['username', 'email', 'phone', 'password1', 'password2', 'address']