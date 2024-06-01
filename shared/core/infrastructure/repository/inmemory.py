import abc
from shared.core.domain import repository


class InMemoryRepository(repository.Repository):

    def __init__(self):
        self.events = dict()

    def get(self, id):
        events = self.events.get(id, [])

        return [self.build_event(e) for e in events]

    def save(self, id, entity):
        if id not in self.events:
            self.events[id] = []
        
        # Save the new events for this entity
        self.events[id].extend([event.to_dict() for event in entity.domain_events])
    
    @abc.abstractmethod
    def build_event(self, e):
        pass