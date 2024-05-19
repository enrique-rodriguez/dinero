from django import urls

from django.shortcuts import render


def view(request):
    return render(request, 'app/home.html')


urlpatterns = [
    urls.path('', view, name='view'),
]