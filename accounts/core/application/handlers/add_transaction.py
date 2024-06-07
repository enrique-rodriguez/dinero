from accounts.core.domain import entities
from accounts.core.domain import values
from accounts.core.domain import events
from accounts.core.domain import repository
from accounts.core.application import commands
from shared.core.application import result
from shared.core.application import handlers


class AddTransactionHandler(handlers.CommandHandler):

    def __init__(self, account_repository: repository.AccountRepository):
        super().__init__()
        self.account_repository = account_repository

    def execute(self, cmd: commands.AddTransactionCommand):
        domain_events = self.account_repository.get(cmd.account_id)
        if not domain_events:
            return result.Result.error(msg=f"Account with id '{cmd.account_id}' does not exists.", code="account-not-found")
        account = entities.Account(domain_events)
        return self.add_transaction(cmd, account)    
    
    def add_transaction(self, cmd: commands.AddTransactionCommand, account: entities.Account):
        res = result.Result.success()

        try:
            account.add_transaction(cmd)
            self.account_repository.save(cmd.account_id, account)
        except ValueError as e:
            res = result.Result.error(str(e), 'transaction-creation-error')
        
        return res
    

class AddTransactionProjectionHandler(handlers.EventHandler):
    def __init__(self, transaction_read_model):
        super().__init__()
        self.transaction_read_model = transaction_read_model

    def dispatch(self, event: events.TransactionAddedEvent):
        print("TODO: Add transaction projection")