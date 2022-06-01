from django.shortcuts import redirect, render
from .forms import RegisterForm, CustomAuthenticationForm, UpdateUserForm, UpdateProfileForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




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


@login_required
def user_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('user_profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form, 
        'profile_form': profile_form
    }
    return render(request, 'user/user_profile.html', context)



# def deneme(request):
#     form_user = UserForm()
#     form_profile = UserProfileForm()

#     if request.method == 'POST':
#         form_user = UserForm(request.POST)
#         form_profile = UserProfileForm(request.POST, request.FILES)

#         if form_user.is_valid() and form_profile.is_valid():
#             user = form_user.save()
#             profile = form_profile.save(commit=False)
#             profile.user = user
#             profile.save()
            
#             login(request, user)
#             messages.success(request, 'Register Succesfull')

#             return redirect('home')

#     context = {
#         "form_user": form_user,
#         "form_profile": form_profile
#     }

#     return render(request, 'users/register.html',context)
