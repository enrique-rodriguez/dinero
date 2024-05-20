from accounts.core.domain import events
from accounts.core.domain.entities import account


class AccountFactory:

    @classmethod
    def create(cls, id, name):
        acct = account.Account(events=[events.AccountAddedEvent(id, name)])

        return acct