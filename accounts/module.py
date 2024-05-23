from shared import module
from accounts.core.domain import events
from accounts.core.application import commands
from accounts.core.application import handlers


class AccountModule(module.Module):

    def __init__(self, account_repository, account_read_model, publisher):
        super().__init__()
        self.publisher = publisher
        self.account_repository = account_repository
        self.account_read_model = account_read_model

        # Commands
        self.register_command(commands.AddAccountCommand, handlers.AddAccountHandler(account_repository))

        # Events
        self.register_event(events.AccountUpdatedEvent, handlers.AccountUpdatedHandler(account_read_model))