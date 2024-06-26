import uuid
from datetime import date
from accounts.core import factories
from accounts.core.domain import events
from accounts.core.domain import models
from accounts.core.domain import repository
from accounts.core.application import commands
from accounts.core.domain.entities.account import Account

from shared.core.application import handlers, result


class AddAccountHandler(handlers.CommandHandler):

    def __init__(self, account_repository: repository.AccountRepository):
        super().__init__()
        self.account_repository = account_repository

    def execute(self, cmd: commands.AddAccountCommand):
        domain_events = self.account_repository.get(cmd.id)
        
        if len(domain_events) > 0:
            return result.Result.error(msg=f"Account with id '{cmd.id}' already exists.", code="account-exists")
            
        res = result.Result.success()
        
        try:
            account = factories.AccountFactory.create(cmd.id, cmd.name, cmd.type, cmd.balance)
            self.account_repository.save(account.id, account)
            evts = account.pop_events()
            evts.extend([events.AccountUpdatedEvent(
                account.id.get(),
                account.name.get(),
                account.category.get(),
                account.type.get(),
                account.balance.get(),
            )])
            self.enqueue_events(evts)
        except ValueError as e:
            res = result.Result.error(f"Could not create account: {str(e)}", "account-creation-error")
        
        return res



class AccountUpdatedHandler(handlers.EventHandler):

    def __init__(self, account_read_model):
        super().__init__()
        self.account_read_model = account_read_model
    
    def dispatch(self, event: events.AccountUpdatedEvent):
        model = self.account_read_model.get(event.account_id)

        if not model:
            model = models.AccountReadModel(account_id=event.account_id)
        
        model.name = event.name
        model.category = event.category
        model.type = event.type
        model.balance = event.balance
        
        self.account_read_model.save(event.account_id, model)


class AccountCreatedHandler(handlers.EventHandler):

    def __init__(self, account_repository):
        super().__init__()
        self.account_repository = account_repository
    
    def dispatch(self, event: events.AccountAddedEvent):
        account_id = event.account_id
        evts = self.account_repository.get(account_id)
        account = Account(evts)

        account.add_transaction(commands.AddTransactionCommand(
            transaction_id=str(uuid.uuid4()),
            account_id=account_id,
            date=date.today().strftime("%Y%m%d"),
            payee_id='0',
            category_id='0',
            memo=''
        ))

        self.account_repository.save(account_id, account)
        self.enqueue_events(account.pop_events())