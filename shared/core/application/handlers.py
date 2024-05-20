import abc


class CommandHandler(abc.ABC):
    
    @abc.abstractmethod
    def execute(self, command):
        pass