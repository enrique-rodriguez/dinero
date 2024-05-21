from accounts.core.domain import events
from accounts.core.domain.entities import account


class AccountFactory:

    @classmethod
    def create(cls, id, name, type, balance):
        acct = account.Account()
        acct.add_event(events.AccountAddedEvent(id, name, type, balance))
        return acct