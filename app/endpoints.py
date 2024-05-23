from django.shortcuts import render


def home(request):
    return render(request, 'app/index.html')


def coming_soon(request):
    return render(request, 'app/coming_soon.html')


def accounts(request):
    return render(request, 'app/accounts/index.html')