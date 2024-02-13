from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CustomUserCreationForm, CustomUserAuthenticationForm


def register_page(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('home:home_page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {email}!')
                return redirect('home:home_page')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
