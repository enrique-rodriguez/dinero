from accounts.core.domain import events
from accounts.core.domain.entities import account


class AccountFactory:

    @classmethod
    def create(cls, id, name, type, balance):
        acct = account.Account()
        acct.add_event(events.AccountAddedEvent(id, name, type, balance))
        return acct
    

class EventFactory:

    @classmethod
    def create(cls, event_name, obj):
        if event_name == events.AccountAddedEvent.__name__:
            return events.AccountAddedEvent.from_dict(obj)