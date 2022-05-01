# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from webApp.forms import (
    RegistrationForm,
    ProfileRegisterForm,
    EditProfileForm
)

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'layout.html')


def editProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/editProfile.html', args)
    

def loginrequest(request):
    form = AuthenticationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            attemptedUser = authenticate(username=username, password=password)

            if attemptedUser is not None:
                login(request, attemptedUser)
                messages.info(request, 'Login Sucessful')
                return redirect('profile')
            else:
                messages.info(request, 'The username or password entered is incorrect, please try again')
                return redirect('login')
    return render(request, "accounts/login.html", context)

def logoutRequest(request):
    logout(request)
    return redirect('login')

# @login_required
# @user_passes_test(lambda user: user.groups.filter(name='Customer').exists())
# def studentAccount(request):
#     return render(request, "accounts/profile.html")

def profile(request):
    return render(request, "accounts/profile.html")

# def register(request):
#     if request.method =='POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('profile')
#     else:
#         form = RegistrationForm()
#         args = {'form': form}
#     return render(request, 'accounts/register.html', args)

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            newUser = authenticate(request, username=username, password=password)
            newUser.is_active = True
            newUser.save()

            if newUser is not None:
                messages.success(request, 'New user account has been created {username}')
            else:
                messages.success(request, 'Error found during new user account generation')

            return redirect("login")
        else:
            messages.success(request, 'Password is too short, please enter an 8 mixed character password ')
    return render(request, "accounts/register.html", {'form': form})
    

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)