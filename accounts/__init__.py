from unittest import mock
from .module import AccountModule

from accounts.core.infrastructure import repository
from accounts.core.infrastructure import readmodel



def get_module(**kwargs):
    account_repository = kwargs.get('account_repository') or repository.DjangoAccountRepository()
    payee_repository = kwargs.get('payee_repository')
    account_read_model = kwargs.get('account_read_model') or readmodel.DjangoAccountReadModelStore()
    publisher = kwargs.get('publisher') or mock.Mock()
    
    return AccountModule(
        account_repository, 
        payee_repository, 
        account_read_model, 
        publisher,
    )


accounts = get_module()