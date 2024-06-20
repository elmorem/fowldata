from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings

from .forms import CreateHuntForm

def all_hunts(request):
    return render(request, 'hunts/all_hunts_by_user.html')


def get_hunt(request):
    pass


def update_hunt(request):
    pass

def create_new_hunt(request):
    context = {
        'user_id': request.user.id,
        'MAPBOX_ACCESS_TOKEN': settings.MAPBOX_ACCESS_TOKEN,
    }
    if request.method == 'POST':
        form = CreateHuntForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
    print(context)
    return render(request, 'hunts/_create_new_hunt.html', context)
@login_required
def create_hunt(request):
    context = {
            'user_id': request.user.id,
            'MAPBOX_ACCESS_TOKEN': settings.MAPBOX_ACCESS_TOKEN,
    }
    if request.method == 'POST':
        form = CreateHuntForm() # does this need to get a request.POST?
        context['form'] = form
        print(f"prointing context from within create_hunt: {context}")
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("hunts/thank_you/")
    else:
        form = CreateHuntForm()
    return render(request, 'hunts/create_hunt.html', context)
