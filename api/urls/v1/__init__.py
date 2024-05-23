from django import urls

from api.views import v1


urlpatterns = [
    urls.path('add_account/', v1.add_account, name='add_account'),
    urls.path('get_balance/', v1.get_balance, name='get-balance'),
    urls.path('get_accounts/', v1.get_accounts, name='get-accounts'),
]