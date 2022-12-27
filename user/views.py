from django.shortcuts import render, redirect
from .form import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def register(request):
    # register_form = UserCreationForm()
    register_form = UserRegistrationForm()
    # if request.method == 'POST':
    #     register_form = UserRegistrationForm(request.POST)
    #     if register_form.is_valid():
    #         register_form.save()
    #         username = register_form.cleaned_data.get('username')
    #         messages.success(request, f'Account was successfully registerd for {username}')
    #         return redirect('/')
    context = {'register_form': register_form}
    return render(request, 'user/register.html', context)