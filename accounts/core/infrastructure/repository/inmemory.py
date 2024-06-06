from accounts.core import factories
from accounts.core.domain import events
from accounts.core.domain.repository import AccountRepository, PayeeRepository
from shared.core.infrastructure.repository import inmemory


class InMemoryAccountRepository(inmemory.InMemoryEventsRepository, AccountRepository):
    
    def count(self):
        return len(self.events)
    
    def build_event(self, obj):
        return factories.EventFactory.create(obj.get("event_name"), obj)
    

class InMemoryPayeeRepository(inmemory.InMemoryRepository, PayeeRepository):
    pass