from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy


def create_account(request):
    context = {}
    return render(request, 'accounts/create_account.html', context)

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    