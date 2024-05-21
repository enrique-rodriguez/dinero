

from django import urls


app_name = "api"


urlpatterns = [
    urls.path('v1/', urls.include('api.urls.v1'))
]