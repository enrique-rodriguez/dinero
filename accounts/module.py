from shared import module

from accounts.core.application import commands
from accounts.core.application import handlers


class AccountModule(module.Module):

    def __init__(self, account_repository):
        super().__init__()
        self.account_repository = account_repository

        self.register_command(commands.AddAccountCommand, handlers.AddAccountHandler(account_repository))
    
