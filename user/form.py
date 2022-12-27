from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from bootstrap_datepicker_plus.widgets import DatePickerInput


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField()
    address = forms.CharField()

    class Meta:
        model= User
        fields =['username', 'email', 'phone', 'password1', 'password2', 'address']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields=['username', 'email',]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['image', 'bio', 'residence']
        widgets = {
        'dob': DatePickerInput
    }
        exclude = ('dob',)