import abc



class MessageHandler(abc.ABC):
    def __init__(self):
        self.event_queue = []

    def collect_events(self):
        events = self.event_queue.copy()
        self.event_queue = []
        return events

    def enqueue_events(self, events):
        self.event_queue.extend(events)


class CommandHandler(MessageHandler):
    
    @abc.abstractmethod
    def execute(self, command):
        pass


class EventHandler(MessageHandler):
    
    @abc.abstractmethod
    def dispatch(self, event):
        pass