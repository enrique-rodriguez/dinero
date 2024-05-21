from .module import AccountModule

from accounts.core.infrastructure import repository



def get_module():
    account_repository = repository.DjangoAccountRepository()
    
    return AccountModule(account_repository)


accounts = get_module()