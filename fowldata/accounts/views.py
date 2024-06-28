from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy, reverse

from .forms import LoginForm, SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:login'))
        if not form.is_valid():
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    print("we are trying to login")
    context = {}
    if request.method == 'POST': 
        form = LoginForm(request.POST)
        context['form'] = form
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('home'))
            else:
                context['error'] = 'Invalid username or password'
                "say that it didn't work"
        if not form.is_valid():
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = LoginForm()
        context['form'] = form
        return render(request, 'accounts/login.html', context)
    
@login_required
def profile(request):
    context = {
        "user": request.user,
        "username": request.user.username,
    }
    return render(request, 'accounts/profile.html', context)
