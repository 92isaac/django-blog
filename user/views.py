from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms  import UserCreationForm
from .form import UserUpdateForm, ProfileUpdateForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# Create your views here.

def register(request):
    # register_form = UserCreationForm()
    register_form = UserRegistrationForm()
    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request, f'Account was successfully registerd for {username}')
            return redirect('/')
        else:
            messages.error(request, 'An error occurred during registration')
    context = {'register_form': register_form}
    return render(request, 'user/register.html', context)



@login_required
def profile(request):
    updateUser = UserUpdateForm()
    updateProfile = ProfileUpdateForm()
    if request.method == 'POST':
        updateUser = UserUpdateForm(request.POST, instance=request.user)
        updateProfile = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if updateUser.is_valid() and updateProfile.is_valid():
            updateUser.save()
            updateProfile.save()

    context={'updateUser': updateUser, 'updateProfile': updateProfile}
    return render(request, 'user/profile.html', context)