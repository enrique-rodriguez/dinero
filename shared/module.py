from shared.core.application import messages

class Module:
    def __init__(self):
        self.command_handlers = {}
    
    def execute(self, command: messages.Command):
        if not self.is_command_registered(command.__class__):
            raise ValueError("Command not registered")

        handler = self.command_handlers.get(command.__class__)

        return handler.execute(command)
        
    def is_command_registered(self, command: messages.Command):
        return self.command_handlers.get(command, None) is not None
    
    def register_command(self, command, handler):
        self.command_handlers[command] = handler
    