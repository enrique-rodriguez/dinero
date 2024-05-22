import abc


class Entity(abc.ABC):
    def __init__(self):
        self.domain_events = []
    
    def pop_events(self):
        events = self.domain_events.copy()
        self.domain_events = []
        return events
    
    def add_event(self, event):
        self.domain_events.append(event)

        self.apply(event)

    @abc.abstractmethod
    def apply(self, event):
        pass