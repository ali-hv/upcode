from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('home:home_page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
