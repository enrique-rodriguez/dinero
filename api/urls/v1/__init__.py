from django import urls

from api.views import v1


urlpatterns = [
    urls.path('add_account/', v1.add_account, name='add_account')
]