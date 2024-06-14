# base level views for the fowldata app
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

