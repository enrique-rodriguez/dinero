from accounts.core.domain import events, values
from accounts.core.domain.entities import account


class AccountFactory:

    @classmethod
    def create(cls, id, name, type, balance):
        acct = account.Account()

        account_id = values.AccountId(id)
        account_name = values.AccountName(name)
        account_type = values.AccountType(type)
        account_balance = values.AccountBalance(balance).clean()
        account_category = values.AccountCategory.from_type(account_type)

        acct.add_event(events.AccountAddedEvent(
            account_id,
            account_name,
            account_type,
            account_category,
            account_balance,
        ))
        
        return acct
    

class EventFactory:

    @classmethod
    def create(cls, event_name, obj):
        event_class = None

        if event_name == events.AccountAddedEvent.__name__:
            event_class = events.AccountAddedEvent
        
        if event_name == events.TransactionAddedEvent.__name__:
            event_class = events.TransactionAddedEvent

        if not event_class:
            raise ValueError(f"Could not map event '{event_name}'")

        return event_class.from_dict(obj)