from django.shortcuts import redirect, render
from .forms import RegisterForm, CustomAuthenticationForm, UpdateUserForm, UpdateProfileForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



#* yeni user oluşturunca ona boş bir profile de oluşturuyorum

def register(request):
    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            profile = Profile(user=user, profile_bio="")
            profile.save()
            login(request, user)
            messages.success(request, 'Register Succesfull')
            return redirect('home')

    context = { 
        'register_form' : register_form
    }

    return render(request, 'user/register.html', context)
            

def user_logout(request):
    logout(request)
    return render(request, 'user/logout.html')

def user_login(request):
    login_form = CustomAuthenticationForm(request, data=request.POST)
    if login_form.is_valid():
        user = login_form.get_user()
        if user:
            messages.success(request, "Login successfull")
            login(request, user)
            return redirect('home')

    return render(request, 'user/login.html', {"form": login_form})


@login_required(login_url='user_login')
def user_profile(request):
    user_form = UpdateUserForm(request.POST or None, instance=request.user)
    profile_form = UpdateProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('home')

    context = {
        'user_form': user_form, 
        'profile_form': profile_form
    }
    return render(request, 'user/user_profile.html', context)

