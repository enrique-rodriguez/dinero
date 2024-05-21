from accounts.core import factories
from accounts.core.application import commands
from accounts.core.domain import repository

from shared.core.application import result
from shared.core.application import handlers


class AddAccountHandler(handlers.CommandHandler):

    def __init__(self, account_repository: repository.AccountRepository):
        self.account_repository = account_repository

    def execute(self, cmd: commands.AddAccountCommand):
        events = self.account_repository.get(cmd.id)
        
        if len(events) > 0:
            return result.Result.error(msg=f"Account with id '{cmd.id}' already exists.", code="account-exists")
            
        return self.add_account(cmd)
            
    def add_account(self, cmd):
        res = result.Result.success()

        try:
            account = factories.AccountFactory.create(cmd.id, cmd.name, cmd._type, cmd.balance)
            self.account_repository.save(cmd.id, account)
        except ValueError as e:
            res = result.Result.error(f"Could not create account: {str(e)}", "account-creation-error")
        
        return res
