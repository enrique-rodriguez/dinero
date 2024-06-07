import accounts
from accounts.core.infrastructure import repository
from accounts.core.infrastructure import readmodel


def get_module(publisher=None):
    account_repository = repository.InMemoryAccountRepository()
    payee_repository = repository.InMemoryPayeeRepository()
    account_read_model = readmodel.InMemoryReadModel()
    transactions_read_model = readmodel.InMemoryReadModel()

    return accounts.get_module(
        account_repository=account_repository, 
        payee_repository=payee_repository,
        account_read_model=account_read_model,
        transactions_read_model=transactions_read_model,
        publisher=publisher,
    )