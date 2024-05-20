from accounts.core.domain.repository import AccountRepository

from shared.core.infrastructure.repository import inmemory


class InMemoryAccountRepository(inmemory.InMemoryRepository, AccountRepository):
    
    def find(self, name):
        for acct in self.entities.values():
            if acct.name.equals(name):
                return acct
        return None

    def count(self):
        return len(self.entities)