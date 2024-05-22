from shared.core.application import handlers
from shared.core.application import messages

class Module:
    def __init__(self):
        self.event_handlers = {}
        self.command_handlers = {}
    
    def execute(self, command: messages.Command):
        if not self.is_command_registered(command.__class__):
            raise ValueError("Command not registered")

        handler: handlers.MessageHandler = self.command_handlers.get(command.__class__)

        res = handler.execute(command)

        evts = handler.collect_events()

        self.dispatch(evts)

        return res
    
    def dispatch(self, events):
        if not isinstance(events, list):
            events = [events]
        
        while len(events) > 0:
            e = events.pop(0)

            for handler in self.event_handlers.get(e.__class__, []):
                handler.dispatch(e)
                events.extend(handler.collect_events())
        
    def is_command_registered(self, command: messages.Command):
        return self.command_handlers.get(command, None) is not None
    
    def register_command(self, command, handler):
        self.command_handlers[command] = handler
    
    def register_event(self, event, handler):
        if self.event_handlers.get(event) is None:
            self.event_handlers[event] = []
        
        self.event_handlers[event].append(handler)
    