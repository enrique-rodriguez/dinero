from accounts.core.domain.repository import AccountRepository

from shared.core.infrastructure.repository import inmemory


class InMemoryAccountRepository(inmemory.InMemoryRepository, AccountRepository):
    
    def count(self):
        return len(self.entities)