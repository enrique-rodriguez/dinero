from django import urls

from app import endpoints

urlpatterns = [
    urls.path('', endpoints.home, name='home'),
]