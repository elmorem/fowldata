from django.shortcuts import render

def create_account(request):
    context = {}
    return render(request, 'accounts/create_account.html', context)
    