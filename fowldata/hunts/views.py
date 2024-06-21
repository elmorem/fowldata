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

# @login_required
def create_hunt(request):
    context = {
            'user_id': request.user.id,
            'MAPBOX_ACCESS_TOKEN': settings.MAPBOX_ACCESS_TOKEN,
    }
    form = CreateHuntForm(request.POST) 
    context['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("hunts/thank_you/")
    else:
        return render(request, 'hunts/create_hunt.html', context)
