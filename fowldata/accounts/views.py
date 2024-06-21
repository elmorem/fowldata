from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy, reverse

from .forms import LoginForm, SignUpForm


def signup(request):
    context = {}
    form = SignUpForm(request.POST)
    context['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(reverse('accounts:login'))
    else:
        return render(request, 'accounts/signup.html', context)

def login(request):
    context = {}
    form = LoginForm(request.POST)
    context['form'] = form
    if request.method == 'POST': 
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(reverse('accounts:login'))
    else:
        return render(request, 'accounts/login.html', context)
