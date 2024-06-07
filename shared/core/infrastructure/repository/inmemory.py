import abc

from shared.core.domain import repository


class InMemoryEventsRepository(repository.Repository):

    def __init__(self):
        self.events = dict()

    def get(self, id):
        key = id

        if not isinstance(id, str):
            key = id.get()

        events = self.events.get(key, [])

        return [self.build_event(e) for e in events]

    def save(self, id, entity):
        key = id

        if not isinstance(id, str):
            key = id.get()

        if key not in self.events:
            self.events[key] = []
        
        # Save the new events for this entity
        self.events[key].extend([event.to_dict() for event in entity.domain_events])
    
    @abc.abstractmethod
    def build_event(self, e):
        pass




class InMemoryRepository(repository.Repository):

    def __init__(self):
        self.objects = dict()

    def get(self, id):
        return self.objects.get(id)

    def save(self, id, entity):
        self.objects[id] = entity
        
    def count(self):
        return len(self.objects)