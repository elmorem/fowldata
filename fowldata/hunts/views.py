from django.shortcuts import render
from django.conf import settings

# Create your views here.

def all_hunts(request):
    return render(request, 'hunts/all_hunts_by_user.html')


def get_hunt(request):
    pass


def update_hunt(request):
    pass


def create_hunt(request):
    context = {
        'user_id': request.user.id,
        'MAPBOX_ACCESS_TOKEN': settings.MAPBOX_ACCESS_TOKEN,

    }
    return render(request, 'hunts/create_hunt.html')
