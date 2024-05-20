from accounts.module import AccountModule
from accounts.core.infrastructure import repository



def create_module():
    account_repository = repository.InMemoryAccountRepository()

    return AccountModule(account_repository)