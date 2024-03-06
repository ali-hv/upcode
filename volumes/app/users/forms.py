from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms

from .models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'تکرار رمز عبور'}))
    phone_number = forms.CharField(max_length=12, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'شماره همراه'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'ایمیل'}))
    
    class Meta:
        model = User
        fields = ("username", "email", "phone_number", )

class CustomUserAuthenticationForm(forms.Form):
    username = None

    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ایمیل'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}))
    
    class Meta:
        model = User
        fields = ("email", "password", )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)
