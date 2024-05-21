from django import urls

from app import endpoints

urlpatterns = [
    urls.path('', endpoints.home, name='home'),
    urls.path('coming_soon/', endpoints.coming_soon, name='coming_soon'),
]