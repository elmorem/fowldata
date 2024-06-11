from django.shortcuts import render

# Create your views here.

def all_hunts(request):
    return render(request, 'hunts/all_hunts_by_user.html')


def get_hunt(request):
    pass


def update_hunt(request):
    pass


def create_hunt(request):
    user_id = request.user.id
